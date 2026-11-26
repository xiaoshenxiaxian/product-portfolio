import { onBeforeUnmount, onMounted, ref } from 'vue'

// 进入视口一次，之后不再重播；减少动效或老浏览器直接视为已进入。
export function useEnter(options = {}) {
  const el = ref(null)
  const shown = ref(false)
  let observer = null

  onMounted(() => {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduced || !('IntersectionObserver' in window) || !el.value) {
      shown.value = true
      return
    }

    observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            shown.value = true
            observer.disconnect()
            observer = null
          }
        }
      },
      {
        threshold: options.threshold ?? 0.28,
        rootMargin: options.rootMargin ?? '0px 0px -8% 0px',
      },
    )
    observer.observe(el.value)
  })

  onBeforeUnmount(() => {
    if (observer) observer.disconnect()
  })

  return { el, shown }
}
