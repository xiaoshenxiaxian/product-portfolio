<script setup>
import { about, nav } from '../data/content'
import { useEnter } from '../composables/useEnter'

const { el, shown } = useEnter({ threshold: 0.3 })
</script>

<template>
  <section id="about" ref="el" class="sec" :class="{ 'is-in': shown }">
    <div class="wrap sec__grid">
      <p class="sec__label">{{ about.label }}</p>

      <div>
        <div class="about">
          <div class="about__intro">
            <h2 class="d2">{{ about.title }}</h2>
            <p class="about__text">{{ about.text }}</p>
            <div class="about__cta">
              <a v-magnetic class="btn" :href="nav.resume.href">
                预览简历
                <span class="btn__icon" data-magnetic-icon aria-hidden="true">→</span>
              </a>
            </div>
            <p class="about__intent">{{ about.intent }}</p>
          </div>

          <dl class="contact">
            <div
              v-for="(item, index) in about.contacts"
              :key="item.k"
              class="contact__row"
              :style="{ '--i': index }"
            >
              <dt>{{ item.k }}</dt>
              <dd>
                <a v-if="item.href" :href="item.href">{{ item.v }}</a>
                <span v-else>{{ item.v }}</span>
                <span v-if="item.meta" class="contact__meta">{{ item.meta }}</span>
              </dd>
            </div>
          </dl>
        </div>

        <div class="about__close">
          <p class="about__closing">
            <span v-for="(line, index) in about.closing" :key="line" :style="{ '--i': index }">
              {{ line }}
            </span>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
