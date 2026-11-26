// 校验线上站点：首页、六个案例页、简历、图片与构建资源。
// 用法：node scripts/verify-live.mjs https://shenjunhui-news.surge.sh
const base = (process.argv[2] || 'https://shenjunhui-news.surge.sh').replace(/\/$/, '')

const html = await (await fetch(base + '/')).text()
const css = (html.match(/href="([^"]+\.css)"/) || [])[1]
const js = (html.match(/src="([^"]+\.js)"/) || [])[1]

const paths = [
  '/',
  '/resume.pdf',
  '/work/huoliyuan.html',
  '/work/yuexi.html',
  '/work/zhuaban.html',
  '/work/zhilan.html',
  '/work/guanjing.html',
  '/work/desktop.html',
  '/work/prd-3.webp',
  '/work/huoliyuan-cover.webp',
  '/docs/huoliyuan-order-prd.pdf',
  '/share.jpg',
  css,
  js,
].filter(Boolean)

let bad = 0
for (const p of paths) {
  try {
    const r = await fetch(base + p, { method: 'HEAD' })
    if (!r.ok) bad += 1
    const type = String(r.headers.get('content-type')).split(';')[0]
    const len = r.headers.get('content-length') || '-'
    console.log(String(r.status).padEnd(4), type.padEnd(26), String(len).padStart(8), p)
  } catch (err) {
    bad += 1
    console.log('ERR ', p, err.message)
  }
}

console.log('title =', (html.match(/<title>(.*?)<\/title>/) || [])[1])
console.log('h1 =', html.includes('把模糊的需求'))
console.log(bad === 0 ? 'LIVE OK' : `LIVE PROBLEMS: ${bad}`)
