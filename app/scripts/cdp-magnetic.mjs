// 验证磁吸按钮：进入光环内读位移，离开后读回位。
// 用法：node scripts/cdp-magnetic.mjs <url> <selector> [out.png]
import { spawn } from 'node:child_process'
import { mkdirSync, writeFileSync } from 'node:fs'
import { dirname } from 'node:path'
import WebSocket from '../../../_ws/node_modules/ws/index.js'

const [url, selector, out] = process.argv.slice(2)
const port = 9700 + Math.floor(Math.random() * 80)
const chrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
const profile = (out ? dirname(out) : process.env.TEMP) + '/prof-' + Date.now()
if (out) mkdirSync(dirname(out), { recursive: true })

const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
const child = spawn(
  chrome,
  [
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--no-first-run',
    `--user-data-dir=${profile}`,
    `--remote-debugging-port=${port}`,
    '--window-size=1440,900',
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
    /* wait */
  }
  await sleep(200)
}
if (!page) {
  child.kill()
  throw new Error('no page target')
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

const evaluate = async (expression) => {
  const res = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true })
  return res.result?.result?.value
}

await send('Page.enable')
await send('Emulation.setDeviceMetricsOverride', {
  width: 1440,
  height: 900,
  deviceScaleFactor: 1,
  mobile: false,
})
await send('Page.navigate', { url })
await sleep(2600)

const rect = await evaluate(
  `(() => { const el = document.querySelector(${JSON.stringify(selector)}); if (!el) return null; const r = el.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height, right: r.right, cy: r.y + r.height / 2 } })()`,
)

if (!rect) {
  console.log('selector not found')
  child.kill()
  process.exit(1)
}

const read = () =>
  evaluate(
    `(() => { const el = document.querySelector(${JSON.stringify(selector)}); const icon = el.querySelector('[data-magnetic-icon]'); return { button: el.style.transform, icon: icon ? icon.style.transform : null, transition: el.style.transition } })()`,
  )

// 光环内：从右边缘外 32px 处进入
const near = { x: Math.round(rect.right + 32), y: Math.round(rect.cy) }
await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: near.x, y: near.y, buttons: 0 })
await sleep(200)
const inside = await read()

// 离开
await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: 20, y: 860, buttons: 0 })
await sleep(180)
const leaving = await read()
await sleep(800)
const settled = await read()

if (out) {
  const shot = await send('Page.captureScreenshot', { format: 'png' })
  writeFileSync(out, Buffer.from(shot.result.data, 'base64'))
}

console.log(JSON.stringify({ rect: { right: Math.round(rect.right), cy: Math.round(rect.cy) }, near, inside, leaving, settled }, null, 2))

ws.close()
child.kill()
await sleep(200)
