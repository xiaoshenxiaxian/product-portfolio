<script setup>
import { works } from '../data/content'
</script>

<template>
  <section id="works" class="sec">
    <div class="wrap sec__grid">
      <p class="sec__label">作品</p>

      <div>
        <div class="sec__head">
          <h2 class="d2">{{ works.title }}</h2>
          <p class="lede">{{ works.lede }}</p>
        </div>

        <ul class="works">
          <li v-for="item in works.items" :key="item.id" class="work">
            <a class="work__link" :href="`/work/${item.id}.html`">
              <span class="work__thumb">
                <img :src="item.thumb" :alt="`${item.name} 原型首页`" loading="lazy" />
              </span>
              <span class="work__body">
                <span class="work__kicker">{{ item.kicker }}</span>
                <h3 class="work__title">{{ item.name }}</h3>
                <p class="work__desc">{{ item.desc }}</p>
              </span>
              <span class="work__more">看详情<span aria-hidden="true">→</span></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>
