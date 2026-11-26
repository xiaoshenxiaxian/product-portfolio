// 逐个滚动到各屏，抓进入中间态与结束态，并读状态。
// 用法：node scripts/cdp-enter.mjs <url> <out-dir>
import { spawn } from 'node:child_process'
import { mkdirSync, writeFileSync } from 'node:fs'
import WebSocket from '../../../_ws/node_modules/ws/index.js'

const [url, outDir] = process.argv.slice(2)
const port = 9250 + Math.floor(Math.random() * 60)
const chrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
const profile = outDir + '/prof-' + Date.now()
mkdirSync(outDir, { recursive: true })

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

const shot = async (name) => {
  const res = await send('Page.captureScreenshot', { format: 'png' })
  writeFileSync(`${outDir}/${name}.png`, Buffer.from(res.result.data, 'base64'))
}

await send('Page.enable')
await send('Emulation.setDeviceMetricsOverride', {
  width: 1440,
  height: 900,
  deviceScaleFactor: 1,
  mobile: false,
})
await send('Page.navigate', { url })
await sleep(2400)

const targets = [
  ['works', '#works'],
  ['grounding', '#grounding'],
  ['about', '#about'],
]

const report = {}

for (const [name, selector] of targets) {
  await evaluate(
    `(() => { const el = document.querySelector(${JSON.stringify(selector)}); window.scrollTo({ top: el.offsetTop + 4, behavior: 'auto' }); })()`,
  )
  await sleep(170)
  await shot(`${name}-mid`)
  await sleep(1400)
  await shot(`${name}-end`)

  report[name] = await evaluate(`(() => {
    const sec = document.querySelector(${JSON.stringify(selector)})
    const isIn = sec.classList.contains('is-in')
    const nodes = [...sec.querySelectorAll('.arc__node')].slice(0, 3).map((el) => ({
      opacity: Number(getComputedStyle(el).opacity).toFixed(2),
      transform: getComputedStyle(el).transform,
    }))
    const stats = [...sec.querySelectorAll('.stat')].map((el) => Number(getComputedStyle(el).opacity).toFixed(2))
    const rows = [...sec.querySelectorAll('.contact__row, .audience tbody tr')].map((el) => Number(getComputedStyle(el).opacity).toFixed(2))
    return { isIn, nodes, stats, rows }
  })()`)
}

console.log(JSON.stringify(report, null, 2))

ws.close()
child.kill()
await sleep(200)
