(async () => {
  const el = document.querySelector('#about')
  el.scrollIntoView({ behavior: 'auto', block: 'start' })
  await new Promise((resolve) => setTimeout(resolve, 1900))
  return { scrolled: true, top: Math.round(window.scrollY) }
})()
