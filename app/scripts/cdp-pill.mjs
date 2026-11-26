// 验证图标按钮展开：读收起/悬停时的宽度与标签透明度。
// 用法：node scripts/cdp-pill.mjs <url> [out.png]
import { spawn } from 'node:child_process'
import { mkdirSync, writeFileSync } from 'node:fs'
import { dirname } from 'node:path'
import WebSocket from '../../../_ws/node_modules/ws/index.js'

const [url, out] = process.argv.slice(2)
const port = 9800 + Math.floor(Math.random() * 70)
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

const snapshot = `
(() => {
  const pills = [...document.querySelectorAll('.nav__actions .pill')]
  return pills.map((el, i) => {
    const r = el.getBoundingClientRect()
    const label = el.querySelector('.pill__label')
    const span = el.querySelector('.pill__label span')
    return {
      i,
      label: el.getAttribute('aria-label'),
      w: Math.round(r.width),
      labelW: Math.round(label.getBoundingClientRect().width),
      opacity: Number(getComputedStyle(span).opacity).toFixed(2),
    }
  })
})()
`

await send('Page.enable')
await send('Emulation.setDeviceMetricsOverride', {
  width: 1440,
  height: 900,
  deviceScaleFactor: 1,
  mobile: false,
})
await send('Page.navigate', { url })
await sleep(2600)

const before = await evaluate(snapshot)

const target = await evaluate(
  `(() => { const el = document.querySelectorAll('.nav__actions .pill')[1]; const r = el.getBoundingClientRect(); return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) } })()`,
)
await send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: target.x, y: target.y, buttons: 0 })
await sleep(650)
const after = await evaluate(snapshot)

if (out) {
  const shot = await send('Page.captureScreenshot', { format: 'png' })
  writeFileSync(out, Buffer.from(shot.result.data, 'base64'))
}

console.log(JSON.stringify({ before, after, at: target }, null, 2))

ws.close()
child.kill()
await sleep(200)
