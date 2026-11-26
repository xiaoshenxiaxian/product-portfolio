<script setup>
import { computed } from 'vue'
import { cases, getCase, neighbours, stories } from './data/cases'
import { nav } from './data/content'
import { useLightbox } from './composables/useLightbox'
import LightboxGallery from './components/LightboxGallery.vue'
import PinnedStory from './components/PinnedStory.vue'
import CursorDot from './components/CursorDot.vue'
import ThemeToggle from './components/ThemeToggle.vue'

const props = defineProps({ slug: { type: String, default: '' } })

const item = computed(() => getCase(props.slug))
const near = computed(() => neighbours(item.value.id))
const story = computed(() => stories[item.value.id])
const { open } = useLightbox()

const gallery = computed(() => ({
  name: item.value.name,
  note: `${item.value.kicker} · ${item.value.gallery.length} 张 · 点击看原图`,
  screens: item.value.gallery,
}))
</script>

<template>
  <a class="skip" href="#main">跳到主要内容</a>

  <header class="case-nav">
    <div class="wrap case-nav__inner">
      <a class="case-nav__brand" href="/">沈俊辉<em>产品助理</em></a>
      <nav class="case-nav__links" aria-label="站内导航">
        <a href="/#works">作品</a>
        <a :href="`/work/${near.next}.html`">下一个案例</a>
        <a class="case-nav__cta" :href="nav.resume.href">简历</a>
        <ThemeToggle />
      </nav>
    </div>
  </header>

  <main id="main" class="case">
    <div class="wrap">
      <p class="case__crumb">
        <a href="/">首页</a>
        <span aria-hidden="true">/</span>
        <a href="/#works">作品</a>
        <span aria-hidden="true">/</span>
        <span>{{ item.name }}</span>
      </p>

      <header class="case__head">
        <p class="case__kicker">
          <span>CASE {{ item.no }}</span>
          {{ item.kicker }}
        </p>
        <h1 class="case__title">{{ item.titleLong || item.name }}</h1>
        <p class="case__sub">{{ item.sub }}</p>

        <dl class="case__meta">
          <div v-for="m in item.meta" :key="m.k">
            <dt>{{ m.k }}</dt>
            <dd>{{ m.v }}</dd>
          </div>
        </dl>
      </header>

      <PinnedStory
        v-if="story"
        :image="story.image"
        :steps="story.steps"
        :label="`${item.name}：分段看图`"
        @zoom="open(gallery)"
      />

      <p v-if="story" class="case__hint">往下滚动：主图会跟着段落推进，点图看大图</p>

      <article class="case__body">
        <section v-for="section in item.sections" :key="section.h" class="case__block">
          <h2 class="case__h2">{{ section.h }}</h2>

          <table v-if="section.table" class="case__table">
            <thead>
              <tr>
                <th v-for="h in section.table.head" :key="h" scope="col">{{ h }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, i) in section.table.rows" :key="i">
                <td v-for="(cell, j) in row" :key="j">{{ cell }}</td>
              </tr>
            </tbody>
          </table>

          <ul v-if="section.bullets" class="case__list">
            <li v-for="b in section.bullets" :key="b">{{ b }}</li>
          </ul>

          <p v-for="p in section.paras || []" :key="p" class="case__p">{{ p }}</p>

          <p v-if="section.links" class="case__links">
            <a
              v-for="l in section.links"
              :key="l.href"
              v-magnetic
              class="btn btn--ghost"
              :href="l.href"
              :download="l.download === false ? null : ''"
              :target="l.download === false ? '_blank' : null"
              :rel="l.download === false ? 'noopener' : null"
            >
              {{ l.label }}
              <span class="btn__icon" data-magnetic-icon aria-hidden="true">
                {{ l.download === false ? '→' : '↓' }}
              </span>
            </a>
          </p>
        </section>

        <p class="case__note">{{ item.note }}</p>

        <p v-if="item.docs" class="case__links case__docs">
          <a
            v-for="doc in item.docs"
            :key="doc.href"
            class="btn btn--ghost"
            :href="doc.href"
          >
            {{ doc.label }}
            <span class="btn__icon" aria-hidden="true">→</span>
          </a>
        </p>
      </article>

      <div v-if="!story" class="case__gallery">
        <a
          v-for="shot in item.gallery"
          :key="shot.src"
          class="case__shot"
          :href="shot.src"
          target="_blank"
          rel="noopener"
          :title="`${shot.alt}（新窗口看原图）`"
        >
          <img :src="shot.src" :alt="shot.alt" loading="lazy" />
        </a>
      </div>

      <nav class="case__pager" aria-label="案例翻页">
        <a :href="`/work/${near.prev}.html`" class="case__pager-link">
          <span>上一个</span>
          {{ cases[near.prev].name }}
        </a>
        <a :href="`/work/${near.next}.html`" class="case__pager-link case__pager-link--next">
          <span>下一个</span>
          {{ cases[near.next].name }}
        </a>
      </nav>
    </div>
  </main>

  <footer class="foot closing">
    <div class="wrap foot__grid">
      <span><b>沈俊辉</b> · 产品助理</span>
      <span>本站为个人作品集，商业信息已脱敏，原型数据为虚构。</span>
      <span>最后更新 2026.11</span>
    </div>
  </footer>

  <LightboxGallery />
  <CursorDot />
</template>
