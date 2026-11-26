<script setup>
import { process } from '../data/content'
</script>

<template>
  <section id="process" class="sec">
    <div class="wrap sec__grid">
      <p class="sec__label">{{ process.label }}</p>

      <div>
        <div class="sec__head">
          <h2 class="d2">{{ process.title }}</h2>
          <p class="lede">{{ process.lede }}</p>
        </div>

        <ol class="steps">
          <li v-for="step in process.steps" :key="step.no" class="step">
            <span class="step__no">{{ step.no }}</span>
            <h3>{{ step.title }}</h3>
            <p>{{ step.text }}</p>
            <span class="step__out">{{ step.out }}</span>
          </li>
        </ol>
      </div>
    </div>
  </section>
</template>
