(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
  let target = null
  for (let i = 0; i < 60; i += 1) {
    const tables = [...document.querySelectorAll('table')]
    target = tables.find((t) => t.textContent.includes('已核销'))
    if (target) break
    await sleep(250)
  }
  if (!target) return { error: 'no table' }
  target.scrollIntoView({ behavior: 'auto', block: 'center' })
  await sleep(900)
  return { rows: [...target.querySelectorAll('tbody tr')].map((r) => r.cells[0].textContent.trim()) }
})()
