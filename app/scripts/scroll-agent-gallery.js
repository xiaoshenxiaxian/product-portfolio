(async () => {
  const el = document.querySelector('.case__gallery')
  el.scrollIntoView({ behavior: 'auto', block: 'center' })
  await new Promise((resolve) => setTimeout(resolve, 2000))
  const imgs = [...el.querySelectorAll('img')].map((img) => ({
    src: img.getAttribute('src'),
    w: img.naturalWidth,
  }))
  return { imgs }
})()
