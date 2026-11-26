<script setup>
import { internship } from '../data/content'
import { useInView } from '../composables/useInView'

const { el, inView } = useInView(0.15)
</script>

<template>
  <section id="internship" ref="el" class="sec spot" :data-in="inView ? 'true' : 'false'">
    <div class="wrap sec__grid">
      <p class="sec__label">{{ internship.label }}</p>

      <div>
        <div class="sec__head">
          <p class="spot__kicker">{{ internship.kicker }}</p>
          <h2 class="d2">{{ internship.title }}</h2>
          <p class="lede">{{ internship.lede }}</p>
        </div>

        <dl class="summary">
          <div v-for="row in internship.summary" :key="row.k">
            <dt>{{ row.k }}</dt>
            <dd>{{ row.v }}</dd>
          </div>
        </dl>

        <div class="spot__foot">
          <a class="link-line" :href="internship.href">
            <span>看完整案例</span>
            <b aria-hidden="true">→</b>
          </a>
          <span class="tag"><i aria-hidden="true"></i>{{ internship.status }}</span>
        </div>

        <div class="frames docs">
          <a v-for="doc in internship.docs" :key="doc.src" class="doc" :href="internship.href">
            <img :src="doc.src" :alt="doc.alt" loading="lazy" />
          </a>
        </div>
      </div>
    </div>
  </section>
</template>
