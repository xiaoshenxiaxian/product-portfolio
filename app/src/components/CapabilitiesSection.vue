<script setup>
import { capabilities } from '../data/content'
</script>

<template>
  <section id="capabilities" class="sec">
    <div class="wrap sec__grid">
      <p class="sec__label">{{ capabilities.label }}</p>

      <div>
        <div class="sec__head">
          <h2 class="d2">{{ capabilities.title }}</h2>
          <p class="lede">{{ capabilities.lede }}</p>
        </div>

        <ul class="caps">
          <li v-for="item in capabilities.items" :key="item.title" class="cap">
            <a class="cap__link" :href="item.href">
              <h3 class="cap__title">{{ item.title }}</h3>
              <p class="cap__text">{{ item.text }}</p>
              <span class="cap__meta">{{ item.meta }}</span>
              <span class="cap__arrow" aria-hidden="true">→</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>
