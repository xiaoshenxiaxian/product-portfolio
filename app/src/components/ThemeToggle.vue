<script setup>
import { onMounted, ref } from 'vue'

const dark = ref(false)

function applyTheme(next) {
  const root = document.documentElement
  if (next === 'dark') {
    root.dataset.theme = 'dark'
  } else {
    delete root.dataset.theme
  }
  dark.value = next === 'dark'
  try {
    localStorage.setItem('theme', next)
  } catch {
    /* 忽略隐私模式下的写入失败 */
  }
}

onMounted(() => {
  dark.value = document.documentElement.dataset.theme === 'dark'
})

function toggle(event) {
  const next = dark.value ? 'light' : 'dark'
  const root = document.documentElement
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  if (!document.startViewTransition || reduced) {
    applyTheme(next)
    return
  }

  const rect = event.currentTarget.getBoundingClientRect()
  const x = rect.left + rect.width / 2
  const y = rect.top + rect.height / 2
  const radius = Math.hypot(
    Math.max(x, window.innerWidth - x),
    Math.max(y, window.innerHeight - y),
  )

  root.classList.add(next === 'dark' ? 'theme-expand' : 'theme-collapse')

  const transition = document.startViewTransition(() => applyTheme(next))

  transition.ready.then(() => {
    const options = { duration: 560, easing: 'cubic-bezier(.4, 0, .2, 1)' }
    if (next === 'dark') {
      root.animate(
        {
          clipPath: [
            `circle(0px at ${x}px ${y}px)`,
            `circle(${radius}px at ${x}px ${y}px)`,
          ],
        },
        { ...options, pseudoElement: '::view-transition-new(root)' },
      )
    } else {
      root.animate(
        {
          clipPath: [
            `circle(${radius}px at ${x}px ${y}px)`,
            `circle(0px at ${x}px ${y}px)`,
          ],
        },
        { ...options, pseudoElement: '::view-transition-old(root)' },
      )
    }
  })

  transition.finished.finally(() => {
    root.classList.remove('theme-expand', 'theme-collapse')
  })
}
</script>

<template>
  <button
    class="theme-toggle"
    type="button"
    :aria-label="dark ? '切换到浅色配色' : '切换到深色配色'"
    :aria-pressed="dark"
    @click="toggle"
  >
    <span class="theme-toggle__icons" aria-hidden="true">
      <svg
        class="theme-sun"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.6"
        stroke-linecap="round"
      >
        <circle cx="12" cy="12" r="4.1" />
        <path d="M12 3.2v2.1M12 18.7v2.1M3.2 12h2.1M18.7 12h2.1M5.8 5.8l1.5 1.5M16.7 16.7l1.5 1.5M18.2 5.8l-1.5 1.5M7.3 16.7l-1.5 1.5" />
      </svg>
      <svg
        class="theme-moon"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.6"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path d="M20.2 14.6A8.2 8.2 0 0 1 9.4 3.8a8.2 8.2 0 1 0 10.8 10.8Z" />
      </svg>
    </span>
  </button>
</template>
