(async () => {
  window.dispatchEvent(new MouseEvent('mousemove', { clientX: 600, clientY: 400, bubbles: true }))
  await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)))
  const el = document.querySelector('.cursor')
  const dot = document.querySelector('.cursor__dot')
  const rect = (node) => {
    if (!node) return null
    const r = node.getBoundingClientRect()
    return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)]
  }
  return {
    fine: matchMedia('(pointer: fine)').matches,
    hoverable: matchMedia('(hover: hover)').matches,
    reduced: matchMedia('(prefers-reduced-motion: reduce)').matches,
    htmlClass: document.documentElement.className,
    cursorClass: el ? el.className : null,
    cursorTransform: el ? el.style.transform : null,
    cursorRect: rect(el),
    dotClass: dot ? dot.className : null,
    dotRect: rect(dot),
    dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
    systemCursor: getComputedStyle(document.body).cursor,
  }
})()
