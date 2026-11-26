(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
  let docs = null
  for (let i = 0; i < 60; i += 1) {
    docs = document.querySelector('.case__docs')
    if (docs) break
    await sleep(250)
  }
  if (!docs) return { error: 'no docs block' }
  docs.scrollIntoView({ behavior: 'auto', block: 'center' })
  await sleep(800)
  return {
    links: [...docs.querySelectorAll('a')].map((a) => ({
      text: a.textContent.trim().replace(/\s+/g, ' '),
      href: a.getAttribute('href'),
      download: a.hasAttribute('download'),
    })),
  }
})()
