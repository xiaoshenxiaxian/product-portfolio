<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'

const props = defineProps({
  image: { type: Object, required: true },
  steps: { type: Array, required: true },
  label: { type: String, default: '' },
})
const emit = defineEmits(['zoom'])

const root = ref(null)
const frame = ref(null)
const imgEl = ref(null)
const stepEls = ref([])

const active = ref(0)
const settled = ref(true)
const reduced = ref(false)

let raf = 0
let size = { w: 0, h: 0 }
let current = { x: 0.5, y: 0.5, z: 1 }
let target = { x: 0.5, y: 0.5, z: 1 }

const clamp = (v, a, b) => Math.min(b, Math.max(a, v))

function measure() {
  if (!frame.value) return
  const rect = frame.value.getBoundingClientRect()
  size = { w: rect.width, h: rect.height }
}

function apply() {
  const img = imgEl.value
  if (!img || !size.w) return
  const tx = (0.5 - current.x) * size.w * current.z
  const ty = (0.5 - current.y) * size.h * current.z
  img.style.transform = `translate3d(${tx}px, ${ty}px, 0) scale(${current.z})`
}

function tick() {
  const el = root.value
  if (el) {
    const rect = el.getBoundingClientRect()
    const total = rect.height - window.innerHeight
    const p = total > 0 ? clamp(-rect.top / total, 0, 1) : 0
    const last = props.steps.length - 1
    const f = p * last
    const i = Math.min(Math.floor(f), Math.max(last - 1, 0))
    const t = last === 0 ? 0 : f - i
    const a = props.steps[i]
    const b = props.steps[Math.min(i + 1, last)]

    target = {
      x: a.x + (b.x - a.x) * t,
      y: a.y + (b.y - a.y) * t,
      z: a.z + (b.z - a.z) * t,
    }
    active.value = Math.round(f)
    settled.value = Math.abs(f - Math.round(f)) < 0.16
  }

  if (reduced.value) {
    current = { ...target }
  } else {
    current = {
      x: current.x + (target.x - current.x) * 0.14,
      y: current.y + (target.y - current.y) * 0.14,
      z: current.z + (target.z - current.z) * 0.14,
    }
  }
  apply()
  raf = requestAnimationFrame(tick)
}

function goTo(index, behavior) {
  const el = root.value
  if (!el) return
  const rect = el.getBoundingClientRect()
  const top = window.scrollY + rect.top
  const total = el.offsetHeight - window.innerHeight
  const ratio = props.steps.length > 1 ? index / (props.steps.length - 1) : 0
  window.scrollTo({
    top: top + total * ratio + 2,
    behavior: behavior || (reduced.value ? 'auto' : 'smooth'),
  })
}

onMounted(() => {
  reduced.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  measure()
  window.addEventListener('resize', measure)
  raf = requestAnimationFrame(tick)

  // ?step=2 直接落到第二段，方便分享与截图
  const wanted = Number(new URLSearchParams(window.location.search).get('step'))
  if (wanted >= 1 && wanted <= props.steps.length) {
    requestAnimationFrame(() => goTo(wanted - 1, 'auto'))
  }
})

onBeforeUnmount(() => {
  cancelAnimationFrame(raf)
  window.removeEventListener('resize', measure)
})

const ringOn = computed(() => settled.value)
</script>

<template>
  <section ref="root" class="story" :aria-label="label">
    <div class="story__media">
      <figure class="story__frame" ref="frame" data-cursor="看大图">
        <img
          ref="imgEl"
          :src="image.src"
          :alt="image.alt"
          @click="emit('zoom')"
        />

        <span class="story__spot" :class="{ 'is-on': ringOn }" aria-hidden="true"></span>
        <span class="story__ring" :class="{ 'is-on': ringOn }" aria-hidden="true"></span>
      </figure>

      <ol class="story__rail" aria-label="分段">
        <li v-for="(step, index) in steps" :key="step.title">
          <button
            type="button"
            :class="{ 'is-on': index === active }"
            :aria-current="index === active ? 'true' : undefined"
            @click="goTo(index)"
          >
            <span>{{ String(index + 1).padStart(2, '0') }}</span>
            {{ step.title }}
          </button>
        </li>
      </ol>
    </div>

    <div class="story__steps">
      <article
        v-for="(step, index) in steps"
        :key="step.title"
        ref="stepEls"
        class="story__step"
        :class="{ 'is-on': index === active }"
      >
        <p class="story__no">{{ String(index + 1).padStart(2, '0') }}</p>
        <h2 class="story__title">{{ step.title }}</h2>
        <p class="story__text">{{ step.text }}</p>

        <img
          class="story__thumb"
          :src="image.src"
          :alt="image.alt"
          :style="{ objectPosition: `${step.x * 100}% ${step.y * 100}%` }"
          loading="lazy"
        />
      </article>
    </div>
  </section>
</template>
