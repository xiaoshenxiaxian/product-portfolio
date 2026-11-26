<script setup>
import { computed, ref } from 'vue'
import { hero } from '../data/content'

const active = ref(0)
const tab = computed(() => hero.tabs[active.value])
</script>

<template>
  <header id="top" class="hero hero--case">
    <div class="wrap hero__inner">
      <div class="hero__copy">
        <p class="hero__role intro intro--1">
          <span class="hero__role-label">{{ hero.roleLabel }}</span>
          <b>{{ hero.roleValue }}</b>
          <span class="hero__role-meta">{{ hero.meta }}</span>
        </p>

        <h1 class="d1 hero__title">
          <span class="line"><span>{{ hero.title }}</span></span>
        </h1>

        <p class="hero__kicker">{{ hero.kicker }}</p>

        <div class="switch" role="tablist" aria-label="实习项目">
          <button
            v-for="(item, index) in hero.tabs"
            :key="item.id"
            class="switch__btn"
            :class="{ 'is-on': index === active }"
            type="button"
            role="tab"
            :aria-selected="index === active"
            @click="active = index"
          >
            {{ item.label }}
          </button>
        </div>

        <Transition name="swap" mode="out-in">
          <div :key="tab.id" class="hero__panel">
            <p class="lede">{{ tab.sub }}</p>

            <dl class="facts facts--3">
              <div v-for="fact in tab.facts" :key="fact.label">
                <dt>{{ fact.n }}</dt>
                <dd>{{ fact.label }}</dd>
              </div>
            </dl>

            <a v-magnetic class="link-line" :href="hero.caseHref">
              <span>{{ hero.cta }}</span>
              <b data-magnetic-icon aria-hidden="true">→</b>
            </a>
          </div>
        </Transition>
      </div>

      <Transition name="swap" mode="out-in">
        <a
          :key="tab.id"
          class="doc-link"
          :href="hero.caseHref"
          data-cursor="看详情"
        >
          <figure class="doc">
            <figcaption class="doc__tab">{{ tab.doc.tab }}</figcaption>
            <img :src="tab.doc.src" :alt="tab.doc.alt" />
          </figure>
        </a>
      </Transition>
    </div>
  </header>
</template>
