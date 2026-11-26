<script setup>
import { computed } from 'vue'
import { navIcons } from './nav-icons'

const props = defineProps({
  icon: { type: String, required: true },
  label: { type: String, required: true },
  href: { type: String, required: true },
  download: { type: Boolean, default: false },
})

const paths = computed(() => navIcons[props.icon] || [])
</script>

<template>
  <a
    class="pill"
    :href="href"
    :download="download ? '' : null"
    :title="label"
    :aria-label="label"
  >
    <span class="pill__icon">
      <svg
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.6"
        stroke-linecap="round"
        stroke-linejoin="round"
        aria-hidden="true"
      >
        <path v-for="d in paths" :key="d" :d="d" />
      </svg>
    </span>
    <span class="pill__label" aria-hidden="true"><span>{{ label }}</span></span>
  </a>
</template>
