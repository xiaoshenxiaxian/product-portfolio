(async () => {
  const img = document.querySelector('img.photo')
  await new Promise((resolve) => setTimeout(resolve, 3000))
  return {
    found: !!img,
    src: img ? img.getAttribute('src') : null,
    complete: img ? img.complete : null,
    natural: img ? [img.naturalWidth, img.naturalHeight] : null,
    rect: img
      ? (() => {
          const r = img.getBoundingClientRect()
          return [Math.round(r.width), Math.round(r.height)]
        })()
      : null,
    bg: img ? getComputedStyle(img).backgroundImage : null,
    opacity: img ? getComputedStyle(img).opacity : null,
  }
})()
