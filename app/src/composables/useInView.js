import { onBeforeUnmount, onMounted, ref } from 'vue'

// 只在主案例里用一次：进入视口后播放，之后不再重播。
export function useInView(threshold = 0.2) {
  const el = ref(null)
  const inView = ref(false)
  let observer = null

  onMounted(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      inView.value = true
      return
    }
    if (!('IntersectionObserver' in window) || !el.value) {
      inView.value = true
      return
    }
    observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            inView.value = true
            observer.disconnect()
            observer = null
          }
        }
      },
      { threshold },
    )
    observer.observe(el.value)
  })

  onBeforeUnmount(() => {
    if (observer) observer.disconnect()
  })

  return { el, inView }
}
