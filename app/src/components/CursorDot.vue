<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'

const dot = ref(null)
const mode = ref('idle')
const label = ref('')
const on = ref(false)

let tx = 0
let ty = 0
let cx = 0
let cy = 0
let raf = 0
let shown = false
let enabled = false

const EASE = 0.18

function frame() {
  const el = dot.value
  if (!el) return
  cx += (tx - cx) * EASE
  cy += (ty - cy) * EASE
  el.style.transform = `translate3d(${cx.toFixed(2)}px, ${cy.toFixed(2)}px, 0)`
  raf = requestAnimationFrame(frame)
}

function onMove(event) {
  tx = event.clientX
  ty = event.clientY
  if (!shown) {
    shown = true
    cx = tx
    cy = ty
    on.value = true
  }
}

function onLeave() {
  shown = false
  on.value = false
}

function hover(event) {
  const target = event.target
  if (!(target instanceof Element)) return

  const marked = target.closest('[data-cursor]')
  if (marked) {
    mode.value = 'media'
    label.value = marked.getAttribute('data-cursor') || '看大图'
    return
  }

  const media = target.closest('img')
  if (media) {
    mode.value = 'media'
    const link = media.closest('a')
    label.value = link ? '看详情' : ''
    return
  }

  if (target.closest('a, button, [role="tab"]')) {
    mode.value = 'link'
    label.value = ''
    return
  }

  mode.value = 'idle'
  label.value = ''
}

onMounted(() => {
  const fine = window.matchMedia('(pointer: fine)').matches
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  enabled = fine && !reduced
  if (!enabled) return

  document.documentElement.classList.add('has-cursor')
  window.addEventListener('mousemove', onMove, { passive: true })
  document.addEventListener('mouseover', hover, { passive: true })
  document.addEventListener('mouseleave', onLeave)
  raf = requestAnimationFrame(frame)
})

onBeforeUnmount(() => {
  if (!enabled) return
  document.documentElement.classList.remove('has-cursor')
  window.removeEventListener('mousemove', onMove)
  document.removeEventListener('mouseover', hover)
  document.removeEventListener('mouseleave', onLeave)
  cancelAnimationFrame(raf)
})
</script>

<template>
  <div ref="dot" class="cursor" :class="{ 'is-on': on }" aria-hidden="true">
    <span class="cursor__dot" :class="`is-${mode}`">
      <span class="cursor__label">{{ label }}</span>
    </span>
  </div>
</template>
