<script setup>
import SiteNav from './components/SiteNav.vue'
import HeroSection from './components/HeroSection.vue'
import ArcWorks from './components/ArcWorks.vue'
import GroundingSection from './components/GroundingSection.vue'
import AboutSection from './components/AboutSection.vue'
import SiteFooter from './components/SiteFooter.vue'
import LightboxGallery from './components/LightboxGallery.vue'
import CursorDot from './components/CursorDot.vue'
</script>

<template>
  <a class="skip" href="#main">跳到主要内容</a>

  <SiteNav />

  <main id="main">
    <HeroSection />
    <ArcWorks />
    <GroundingSection />
    <AboutSection />
  </main>

  <SiteFooter />
  <LightboxGallery />
  <CursorDot />
</template>
