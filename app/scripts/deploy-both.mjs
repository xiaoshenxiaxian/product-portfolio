// 一键发布：把 dist 同时发到主域名与旧域名
// 用法：
//   node scripts/deploy-both.mjs           （直接发布现有 dist）
//   node scripts/deploy-both.mjs --build   （先构建再发布）
import { execFileSync, execSync } from 'node:child_process'
import { existsSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'

const ROOT = resolve(import.meta.dirname, '..')
const DIST = resolve(ROOT, 'dist')
const SURGE = process.env.SURGE_BIN || resolve(ROOT, '..', '_surge/node_modules/surge/bin/surge')
const DOMAINS = ['shenjunhui.cn', 'shenjunhui-news.surge.sh']
const doBuild = process.argv.includes('--build')

if (doBuild) {
  console.log('\n▶ 构建 dist')
  execSync('npm.cmd run build', { cwd: ROOT, stdio: 'inherit' })
}

if (!existsSync(DIST)) {
  console.error('dist 不存在：先 npm run build，或用 --build')
  process.exit(1)
}

writeFileSync(resolve(DIST, 'CNAME'), DOMAINS[0], 'ascii')

for (const d of DOMAINS) {
  console.log(`\n▶ 发布到 ${d}`)
  try {
    execFileSync(process.execPath, [SURGE, DIST, d], { cwd: ROOT, stdio: 'inherit' })
  } catch {
    // surge CLI 成功时也可能返回非 0，以最后的 HTTP 验证为准
    console.log('  (surge 退出码非 0，继续)')
  }
}

for (const d of DOMAINS) {
  try {
    const res = await fetch(`https://${d}/`, { method: 'HEAD' })
    console.log(`✓ ${d} -> HTTP ${res.status}`)
  } catch (e) {
    console.log(`✗ ${d} -> ${e.cause?.code || e.message}（本机 DNS 未更新时正常）`)
  }
}

console.log('\n完成：' + DOMAINS.join(' / '))
