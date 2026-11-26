// 用 CDP 拍一张指定滚动位置的视口截图（默认等页面完全就绪）。
// 用法：node scripts/cdp-shot.mjs <url> <out.png> [width] [height] [waitMs]
import { spawn } from 'node:child_process'
import { mkdirSync, writeFileSync } from 'node:fs'
import { dirname } from 'node:path'
import WebSocket from '../../../_ws/node_modules/ws/index.js'

const [url, out, w = '1440', h = '900', wait = '2600'] = process.argv.slice(2)
const port = 9400 + Math.floor(Math.random() * 90)
const chrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
const profile = dirname(out) + '/prof-' + Date.now()
mkdirSync(dirname(out), { recursive: true })

const sleep = (ms) => new Promise((r) => setTimeout(r, ms))

const child = spawn(
  chrome,
  [
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--no-first-run',
    '--no-default-browser-check',
    `--user-data-dir=${profile}`,
    `--remote-debugging-port=${port}`,
    `--window-size=${w},${h}`,
    'about:blank',
  ],
  { stdio: 'ignore' },
)

async function getJson(path) {
  const res = await fetch(`http://127.0.0.1:${port}${path}`)
  return res.json()
}

let page = null
for (let i = 0; i < 80; i += 1) {
  try {
    const list = await getJson('/json/list')
    page = list.find((t) => t.type === 'page')
    if (page) break
  } catch {
    /* not up yet */
  }
  await sleep(200)
}
if (!page) {
  child.kill()
  throw new Error('chrome did not expose a page target')
}

const ws = new WebSocket(page.webSocketDebuggerUrl)
await new Promise((resolve, reject) => {
  ws.once('open', resolve)
  ws.once('error', reject)
})

let seq = 0
const pending = new Map()
ws.on('message', (data) => {
  const msg = JSON.parse(data)
  if (msg.id && pending.has(msg.id)) {
    pending.get(msg.id)(msg)
    pending.delete(msg.id)
  }
})
const send = (method, params = {}) =>
  new Promise((resolve) => {
    const id = ++seq
    pending.set(id, resolve)
    ws.send(JSON.stringify({ id, method, params }))
  })

await send('Page.enable')
await send('Emulation.setDeviceMetricsOverride', {
  width: Number(w),
  height: Number(h),
  deviceScaleFactor: 1,
  mobile: false,
})
await send('Page.navigate', { url })
await sleep(Number(wait))
const shot = await send('Page.captureScreenshot', { format: 'png' })
writeFileSync(out, Buffer.from(shot.result.data, 'base64'))
console.log('saved', out)

ws.close()
child.kill()
await sleep(300)
