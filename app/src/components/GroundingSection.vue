<script setup>
import { grounding } from '../data/content'
import { useEnter } from '../composables/useEnter'

const { el, shown } = useEnter({ threshold: 0.3 })
</script>

<template>
  <section id="grounding" ref="el" class="sec" :class="{ 'is-in': shown }">
    <div class="wrap sec__grid">
      <p class="sec__label">{{ grounding.label }}</p>

      <div>
        <div class="sec__head">
          <h2 class="d2">{{ grounding.title }}</h2>
          <p class="lede">{{ grounding.lede }}</p>
        </div>

        <div class="ground">
          <div>
            <p class="lede">
              店里没有用户研究员，只有每天来的人。谁在挑、挑多久、最后买了哪一件，站一天就看见了；哪件货压在架上，月末算一遍动销率就知道。
            </p>

            <div class="stats">
              <div
                v-for="(stat, index) in grounding.stats"
                :key="stat.label"
                class="stat"
                :style="{ '--i': index }"
              >
                <b>{{ stat.n }}</b>
                <span>{{ stat.label }}</span>
              </div>
            </div>
          </div>

          <table class="audience">
            <caption class="sr-only">三类客群的诉求与我做的调整</caption>
            <thead>
              <tr>
                <th scope="col">客群</th>
                <th scope="col">她们的诉求</th>
                <th scope="col">我改了什么</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(row, index) in grounding.audience.rows"
                :key="row[0]"
                :style="{ '--i': index }"
              >
                <th scope="row">{{ row[0] }}</th>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>
