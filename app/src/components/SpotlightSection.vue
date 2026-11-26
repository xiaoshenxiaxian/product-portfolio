<script setup>
import PhoneFrame from './PhoneFrame.vue'
import { projects, spotlight } from '../data/content'
import { useInView } from '../composables/useInView'
import { useLightbox } from '../composables/useLightbox'

const { el, inView } = useInView(0.15)
const { open } = useLightbox()
const project = projects[spotlight.projectId]
</script>

<template>
  <section id="spotlight" ref="el" class="sec spot" :data-in="inView ? 'true' : 'false'">
    <div class="wrap sec__grid">
      <p class="sec__label">{{ spotlight.label }}</p>

      <div>
        <div class="sec__head">
          <h2 class="d2">{{ spotlight.title }}</h2>
          <p class="lede">{{ spotlight.lede }}</p>
        </div>

        <dl class="summary">
          <div v-for="row in spotlight.summary" :key="row.k">
            <dt>{{ row.k }}</dt>
            <dd>{{ row.v }}</dd>
          </div>
        </dl>

        <div class="spot__foot">
          <button class="link-line" type="button" @click="open(project)">
            <span>{{ spotlight.cta }}</span>
            <b aria-hidden="true">→</b>
          </button>
          <span class="tag"><i aria-hidden="true"></i>{{ spotlight.status }}</span>
        </div>

        <div class="frames">
          <PhoneFrame
            v-for="screen in project.screens"
            :key="screen.src"
            :src="screen.src"
            :alt="screen.alt"
          />
        </div>
      </div>
    </div>
  </section>
</template>
