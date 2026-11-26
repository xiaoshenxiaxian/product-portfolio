<script setup>
import { cases, projects } from '../data/content'
import { useLightbox } from '../composables/useLightbox'

const { open } = useLightbox()
</script>

<template>
  <section id="cases" class="sec">
    <div class="wrap sec__grid">
      <p class="sec__label">案例</p>

      <div>
        <div class="sec__head">
          <h2 class="d2">另外三个项目，和一次付费墙尝试</h2>
          <p class="lede">每个项目都从一句问题开始：用户在哪一步走不下去。</p>
        </div>

        <table class="cases">
          <caption class="sr-only">项目索引：名称、要解决的问题与证据</caption>
          <thead>
            <tr>
              <th scope="col"><span class="sr-only">预览</span></th>
              <th scope="col">项目</th>
              <th scope="col">要解决的问题</th>
              <th scope="col">证据</th>
              <th scope="col"><span class="sr-only">查看屏幕</span></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in cases" :key="item.id">
              <td class="cases__thumb">
                <img :src="item.thumb" :alt="`${item.name} 的原型首页`" loading="lazy" width="46" height="97" />
              </td>
              <td>
                <span class="cases__name">{{ item.name }}<em>{{ item.kind }}</em></span>
              </td>
              <td class="cases__problem">{{ item.problem }}</td>
              <td class="cases__proof">{{ item.proof }}</td>
              <td class="cases__action">
                <button
                  class="row-open"
                  type="button"
                  :aria-label="`查看${item.name}的原型屏幕`"
                  @click="open(projects[item.id])"
                >
                  <span class="row-open__label">看屏幕</span>
                  <span aria-hidden="true">→</span>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
