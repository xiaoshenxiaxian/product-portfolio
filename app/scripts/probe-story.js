(() => {
  const pick = (sel) => document.querySelector(sel)
  const rect = (el) => {
    if (!el) return null
    const b = el.getBoundingClientRect()
    return { x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.width), h: Math.round(b.height) }
  }
  const frame = pick('.story__frame')
  const ring = pick('.story__ring')
  const img = pick('.story__frame img')
  const cs = ring ? getComputedStyle(ring) : null
  return {
    scrollY: Math.round(window.scrollY),
    frame: rect(frame),
    ring: rect(ring),
    img: rect(img),
    imgTransform: img ? img.style.transform : '',
    ringStyle: cs
      ? {
          left: cs.left,
          top: cs.top,
          width: cs.width,
          height: cs.height,
          marginLeft: cs.marginLeft,
          marginTop: cs.marginTop,
          opacity: cs.opacity,
          position: cs.position,
        }
      : null,
  }
})()
