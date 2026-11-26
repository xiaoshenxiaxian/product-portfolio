(async () => {
  await new Promise((resolve) => setTimeout(resolve, 1800))
  const pills = [...document.querySelectorAll('.nav__actions .pill')].map((a) => ({
    label: a.getAttribute('aria-label'),
    href: a.getAttribute('href'),
    download: a.hasAttribute('download'),
  }))
  const aboutBtn = document.querySelector('#about .btn')
  return {
    pills,
    aboutCta: aboutBtn ? { text: aboutBtn.textContent.trim(), href: aboutBtn.getAttribute('href') } : null,
  }
})()
