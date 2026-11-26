(async () => {
  const el = document.querySelector('#works')
  el.scrollIntoView({ behavior: 'auto', block: 'center' })
  await new Promise((resolve) => setTimeout(resolve, 2200))
  return { nodes: document.querySelectorAll('.arc__node').length }
})()
