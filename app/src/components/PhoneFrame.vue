<script setup>
defineProps({
  src: { type: String, required: true },
  alt: { type: String, default: '' },
  tab: { type: String, default: '' },
  eager: { type: Boolean, default: false },
})
</script>

<template>
  <div class="phone">
    <span v-if="tab" class="phone__tab">{{ tab }}</span>
    <div class="phone__frame">
      <img :src="src" :alt="alt" :loading="eager ? 'eager' : 'lazy'" decoding="async" />
    </div>
  </div>
</template>
