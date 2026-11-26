import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'node:path'

export default defineConfig({
  base: '/',
  plugins: [vue()],
  build: {
    target: 'es2019',
    assetsInlineLimit: 0,
    rollupOptions: {
      input: {
        main: resolve(import.meta.dirname, 'index.html'),
        huoliyuan: resolve(import.meta.dirname, 'work/huoliyuan.html'),
        yuexi: resolve(import.meta.dirname, 'work/yuexi.html'),
        zhuaban: resolve(import.meta.dirname, 'work/zhuaban.html'),
        zhilan: resolve(import.meta.dirname, 'work/zhilan.html'),
        guanjing: resolve(import.meta.dirname, 'work/guanjing.html'),
        desktop: resolve(import.meta.dirname, 'work/desktop.html'),
        agent: resolve(import.meta.dirname, 'work/agent.html'),
        'agent-demo': resolve(import.meta.dirname, 'work/agent-demo.html'),
      },
    },
  },
})
