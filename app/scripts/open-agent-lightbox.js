(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
  let btn = null
  for (let i = 0; i < 60; i += 1) {
    btn = document.querySelector('.case__shot')
    if (btn) break
    await sleep(250)
  }
  if (!btn) return { error: 'no gallery button' }
  btn.scrollIntoView({ behavior: 'auto', block: 'center' })
  await sleep(1200)
  btn.click()
  await sleep(2500)
  const dialog = document.querySelector('dialog.lb')
  const imgs = dialog ? [...dialog.querySelectorAll('img')].map((i) => [i.naturalWidth, Math.round(i.getBoundingClientRect().width)]) : []
  return { open: dialog ? dialog.open : false, imgs }
})()
