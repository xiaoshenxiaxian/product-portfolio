(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
  let grid = null
  for (let i = 0; i < 60; i += 1) {
    grid = document.querySelector('.case__gallery')
    if (grid) break
    await sleep(250)
  }
  if (!grid) return { error: 'no gallery' }
  grid.scrollIntoView({ behavior: 'auto', block: 'center' })
  await sleep(1500)
  const links = [...grid.querySelectorAll('a.case__shot')].map((a) => ({
    href: a.getAttribute('href'),
    target: a.getAttribute('target'),
    w: a.querySelector('img').naturalWidth,
    shown: Math.round(a.getBoundingClientRect().width),
  }))
  return { links }
})()
