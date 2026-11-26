// 检查线上页面是否都带主题预置脚本，并对比资源指纹。
const base = (process.argv[2] || 'https://shenjunhui-news.surge.sh').replace(/\/$/, '')

const pages = [
  '/',
  '/work/huoliyuan.html',
  '/work/yuexi.html',
  '/work/zhuaban.html',
  '/work/zhilan.html',
  '/work/guanjing.html',
  '/work/desktop.html',
]

let ok = 0
for (const path of pages) {
  const res = await fetch(base + path)
  const html = await res.text()
  const hasScript = html.includes("localStorage.getItem('theme')")
  const main = (html.match(/assets\/(main|case|theme|sections|cursor)-[A-Za-z0-9_-]+\.js/) || [])[0] || '-'
  if (hasScript) ok += 1
  console.log(String(res.status), hasScript ? 'theme-script ✓' : 'theme-script ✗', main.padEnd(30), path)
}

console.log(ok === pages.length ? 'ALL PAGES OK' : `MISSING ON ${pages.length - ok} PAGES`)
