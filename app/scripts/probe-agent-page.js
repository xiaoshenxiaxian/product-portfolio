(async () => {
  await new Promise((resolve) => setTimeout(resolve, 1500))
  const link = document.querySelector('.case__links a')
  const imgs = [...document.querySelectorAll('.case__gallery img, .gallery img')].map((img) => ({
    src: img.getAttribute('src'),
    w: img.naturalWidth,
  }))
  return {
    link: link
      ? {
          text: link.textContent.trim(),
          href: link.getAttribute('href'),
          download: link.hasAttribute('download'),
          target: link.getAttribute('target'),
        }
      : null,
    imgs,
  }
})()
