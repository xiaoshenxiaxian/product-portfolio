// 预览 dist 的极简静态服务器：不派生子进程，方便在受限环境里跑。
// 用法：node scripts/serve-dist.mjs [port]
import { createServer } from 'node:http'
import { createReadStream, existsSync, statSync } from 'node:fs'
import { extname, join, normalize } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../dist/', import.meta.url))
const port = Number(process.argv[2] || 4173)

const types = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.webp': 'image/webp',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.pdf': 'application/pdf',
  '.woff2': 'font/woff2',
  '.json': 'application/json; charset=utf-8',
}

createServer((req, res) => {
  const url = decodeURIComponent((req.url || '/').split('?')[0])
  let file = join(root, normalize(url === '/' ? '/index.html' : url))

  if (!file.startsWith(root)) {
    res.writeHead(403).end('forbidden')
    return
  }
  if (!existsSync(file) || statSync(file).isDirectory()) {
    const fallback = join(root, 'index.html')
    if (existsSync(fallback)) {
      res.writeHead(200, { 'content-type': types['.html'] })
      createReadStream(fallback).pipe(res)
      return
    }
    res.writeHead(404).end('not found')
    return
  }

  res.writeHead(200, { 'content-type': types[extname(file).toLowerCase()] || 'application/octet-stream' })
  createReadStream(file).pipe(res)
}).listen(port, '127.0.0.1', () => {
  console.log(`serving ${root} on http://127.0.0.1:${port}/`)
})
