(async () => {
  const mode = window.__mode || 'table'
  const target =
    mode === 'table'
      ? document.querySelector('table')
      : document.querySelector('.case__links')
  target.scrollIntoView({ behavior: 'auto', block: 'center' })
  await new Promise((resolve) => setTimeout(resolve, 1600))
  return { mode, found: !!target }
})()
