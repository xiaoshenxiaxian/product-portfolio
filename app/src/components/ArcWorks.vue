<script setup>
import { works } from '../data/content'
import { useEnter } from '../composables/useEnter'

const { el, shown } = useEnter({ threshold: 0.24 })

// 五个项目沿一条抛物线散开；位置与背后的虚线共用同一条曲线。
const nodes = works.items.map((item, index) => {
  const t = index / (works.items.length - 1)
  return {
    ...item,
    index,
    style: {
      left: `${8 + 84 * t}%`,
      top: `${64 - 34 * Math.sin(Math.PI * t)}%`,
      '--i': index,
    },
  }
})
</script>

<template>
  <section id="works" ref="el" class="sec arc-sec" :class="{ 'is-in': shown }">
    <div class="wrap arc-wrap">
      <div class="arc-head">
        <p class="sec__label">{{ works.label }}</p>
        <h2 class="arc-title">{{ works.title }}</h2>
        <p class="arc-lede">{{ works.lede }}</p>
      </div>

      <div class="arc">
        <svg class="arc__line" viewBox="0 0 1000 540" preserveAspectRatio="none" aria-hidden="true">
          <path d="M 80 345.6 Q 500 -21.6 920 345.6" />
        </svg>

        <a
          v-for="node in nodes"
          :key="node.id"
          class="arc__node"
          :style="node.style"
          :href="`/work/${node.id}.html`"
          :aria-label="`${node.name}，${node.kicker}，查看详情`"
        >
          <img
            :src="node.thumb"
            :alt="node.alt"
            width="360"
            height="779"
            decoding="async"
            loading="lazy"
          />
          <span class="arc__name">
            {{ node.name }}
            <em>{{ node.kicker }}</em>
          </span>
        </a>
      </div>
    </div>
  </section>
</template>
