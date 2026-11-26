<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import NavPill from './NavPill.vue'
import ThemeToggle from './ThemeToggle.vue'
import { nav } from '../data/content'

const solid = ref(false)
let frame = 0

function onScroll() {
  if (frame) return
  frame = requestAnimationFrame(() => {
    solid.value = window.scrollY > 24
    frame = 0
  })
}

onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
  if (frame) cancelAnimationFrame(frame)
})
</script>

<template>
  <header class="nav" :class="{ 'nav--solid': solid }">
    <div class="nav__inner">
      <a class="nav__brand" href="#top">沈俊辉<em>产品助理</em></a>

      <nav class="nav__actions" aria-label="站内导航">
        <NavPill
          v-for="item in nav.pills"
          :key="item.href"
          v-bind="item"
          :class="{ 'pill--resume': item.icon === 'resume' }"
        />
        <ThemeToggle />
      </nav>
    </div>
  </header>
</template>
