<script setup>
import { nextTick, ref, watch } from 'vue'
import { useLightbox } from '../composables/useLightbox'

const { project, close } = useLightbox()
const dialog = ref(null)

watch(project, async (value) => {
  const el = dialog.value
  if (!el) return

  if (value) {
    if (!el.open) el.showModal()
    await nextTick()
    el.querySelector('.lb__close')?.focus()
  } else if (el.open) {
    el.close()
  }
})

function onCancel(event) {
  event.preventDefault()
  close()
}

function onBackdrop(event) {
  if (event.target === dialog.value) close()
}
</script>

<template>
  <dialog ref="dialog" class="lb" aria-labelledby="lb-title" @cancel="onCancel" @click="onBackdrop">
    <div v-if="project" class="lb__inner">
      <div class="lb__head">
        <div>
          <h2 id="lb-title" class="lb__title">{{ project.name }}</h2>
          <p class="lb__note">{{ project.note }}</p>
        </div>
        <button class="lb__close" type="button" @click="close">关闭</button>
      </div>

      <div class="lb__screens">
        <img v-for="screen in project.screens" :key="screen.src" :src="screen.src" :alt="screen.alt" />
      </div>
    </div>
  </dialog>
</template>
