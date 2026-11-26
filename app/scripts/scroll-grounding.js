(async () => {
  const el = document.querySelector('#grounding')
  el.scrollIntoView({ behavior: 'auto', block: 'start' })
  await new Promise((resolve) => setTimeout(resolve, 2000))
  const stats = [...el.querySelectorAll('.stat')].map((s) => s.textContent.trim().replace(/\s+/g, ' '))
  return { stats }
})()
