(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
  let target = null
  for (let i = 0; i < 60; i += 1) {
    target = [...document.querySelectorAll('h2')].find((h) => h.textContent.includes('为什么给一个 Agent 做评测'))
    if (target) break
    await sleep(250)
  }
  if (!target) return { error: 'not found' }
  target.scrollIntoView({ behavior: 'auto', block: 'start' })
  await sleep(1200)
  return { ok: true, text: target.textContent.trim(), y: window.scrollY }
})()
