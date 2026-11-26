// v-magnetic：鼠标进入按钮外 60px 光环内，按钮按偏移量的 0.35 倍跟随，
// 内部图标额外跟随 0.15 倍；离开后弹性回位。
const EASE = 'cubic-bezier(.34,1.56,.64,1)'
const SPRING_MS = 620
const MAX_PULL = 40

export default {
  mounted(el, binding) {
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return

    const options = binding.value && typeof binding.value === 'object' ? binding.value : {}
    const range = options.range ?? 60
    const pull = options.strength ?? 0.35
    const iconPull = options.iconStrength ?? 0.15
    const icon = el.querySelector('[data-magnetic-icon]')

    let curX = 0
    let curY = 0
    let inside = false

    el.style.willChange = 'transform'
    if (icon) icon.style.willChange = 'transform'

    const spring = (node, x, y) => {
      node.style.transition = `transform ${SPRING_MS}ms ${EASE}`
      node.style.transform = `translate3d(${x}px, ${y}px, 0)`
    }

    const follow = (node, x, y) => {
      node.style.transition = 'none'
      node.style.transform = `translate3d(${x}px, ${y}px, 0)`
    }

    const clamp = (value) => Math.max(-MAX_PULL, Math.min(MAX_PULL, value))

    const onMove = (event) => {
      const rect = el.getBoundingClientRect()
      const baseX = rect.left - curX
      const baseY = rect.top - curY
      const ox = event.clientX - (baseX + rect.width / 2)
      const oy = event.clientY - (baseY + rect.height / 2)
      const dx = Math.max(baseX - event.clientX, 0, event.clientX - (baseX + rect.width))
      const dy = Math.max(baseY - event.clientY, 0, event.clientY - (baseY + rect.height))
      const distance = Math.hypot(dx, dy)

      if (distance <= range) {
        inside = true
        curX = clamp(ox * pull)
        curY = clamp(oy * pull)
        follow(el, curX, curY)
        if (icon) follow(icon, clamp(ox * iconPull), clamp(oy * iconPull))
        return
      }

      if (inside) {
        inside = false
        curX = 0
        curY = 0
        spring(el, 0, 0)
        if (icon) spring(icon, 0, 0)
      }
    }

    window.addEventListener('mousemove', onMove, { passive: true })
    el.__magneticCleanup = () => {
      window.removeEventListener('mousemove', onMove)
      el.style.transform = ''
      el.style.transition = ''
      if (icon) {
        icon.style.transform = ''
        icon.style.transition = ''
      }
    }
  },

  unmounted(el) {
    if (el.__magneticCleanup) el.__magneticCleanup()
  },
}
