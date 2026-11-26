// 用 Chrome 打印成 PDF（保留 @page A4 与背景色）。
// 用法：node scripts/print-pdf.mjs <url> <out.pdf>
import { spawn } from 'node:child_process'
import { mkdirSync, writeFileSync } from 'node:fs'
import { dirname } from 'node:path'
import WebSocket from '../../../_ws/node_modules/ws/index.js'

const [url, out] = process.argv.slice(2)
const port = 9150 + Math.floor(Math.random() * 60)
const chrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
const profile = dirname(out) + '/prof-' + Date.now()
mkdirSync(dirname(out), { recursive: true })

const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
const child = spawn(
  chrome,
  [
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    `--user-data-dir=${profile}`,
    `--remote-debugging-port=${port}`,
    '--window-size=1280,900',
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

await send('Page.enable')
await send('Page.navigate', { url })
await sleep(2600)

const pdf = await send('Page.printToPDF', {
  printBackground: true,
  preferCSSPageSize: true,
  marginTop: 0,
  marginBottom: 0,
  marginLeft: 0,
  marginRight: 0,
})

if (!pdf.result?.data) {
  console.log(JSON.stringify(pdf).slice(0, 400))
  child.kill()
  process.exit(1)
}

const buffer = Buffer.from(pdf.result.data, 'base64')
writeFileSync(out, buffer)
console.log('saved', out, buffer.length, 'bytes')

ws.close()
child.kill()
await sleep(200)
