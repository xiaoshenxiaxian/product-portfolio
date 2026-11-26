<script setup>
import { computed, ref } from 'vue'
import { demoCases } from './data/agentDemo'
import { nav } from './data/content'
import ThemeToggle from './components/ThemeToggle.vue'

const activeId = ref(demoCases[0].id)
const active = computed(() => demoCases.find((c) => c.id === activeId.value) || demoCases[0])

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}
function inline(s) {
  return esc(s)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
}
function render(text) {
  const lines = text.split('\n')
  const out = []
  let i = 0
  while (i < lines.length) {
    const line = lines[i].trim()
    if (!line) { i += 1; continue }
    if (/^#{1,4}\s/.test(line)) {
      const lvl = Math.min(6, line.match(/^#+/)[0].length + 1)
      out.push(`<h${lvl}>${inline(line.replace(/^#+\s*/, ''))}</h${lvl}>`)
      i += 1
      continue
    }
    if (line.startsWith('|')) {
      const rows = []
      while (i < lines.length && lines[i].trim().startsWith('|')) { rows.push(lines[i].trim()); i += 1 }
      const cells = rows
        .map((r) => r.split('|').slice(1, -1).map((c) => c.trim()))
        .filter((r) => r.length && !r.every((c) => /^:?-{2,}:?$/.test(c)))
      if (cells.length) {
        const head = cells[0].map((c) => `<th>${inline(c)}</th>`).join('')
        const body = cells.slice(1).map((r) => `<tr>${r.map((c) => `<td>${inline(c)}</td>`).join('')}</tr>`).join('')
        out.push(`<table><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table>`)
      }
      continue
    }
    if (/^[-·•]\s/.test(line)) {
      const items = []
      while (i < lines.length && /^[-·•]\s/.test(lines[i].trim())) {
        items.push(inline(lines[i].trim().replace(/^[-·•]\s*/, '')))
        i += 1
      }
      out.push(`<ul>${items.map((t) => `<li>${t}</li>`).join('')}</ul>`)
      continue
    }
    out.push(`<p>${inline(line)}</p>`)
    i += 1
  }
  return out.join('')
}

const html = computed(() => render(active.value.output))
</script>

<template>
  <a class="skip" href="#main">跳到主要内容</a>

  <header class="case-nav">
    <div class="wrap case-nav__inner">
      <a class="case-nav__brand" href="/">沈俊辉<em>产品助理</em></a>
      <nav class="case-nav__links" aria-label="站内导航">
        <a href="/#works">作品</a>
        <a href="/work/agent.html">返回案例</a>
        <a class="case-nav__cta" :href="nav.resume.href">简历</a>
        <ThemeToggle />
      </nav>
    </div>
  </header>

  <main id="main" class="demo">
    <div class="wrap">
      <p class="case__crumb">
        <a href="/">首页</a><span aria-hidden="true">/</span>
        <a href="/#works">作品</a><span aria-hidden="true">/</span>
        <a href="/work/agent.html">需求拆解 Agent</a><span aria-hidden="true">/</span>
        <span>演示</span>
      </p>

      <p class="demo__kick">DEMO · 真实运行结果</p>
      <h1 class="demo__title">需求拆解 Agent：选一条输入，看它怎么拆</h1>
      <p class="demo__lead">
        下面是 6 条真实用例，输出是 2026-11-25 用 v3.2 提示词跑出来的原始结果，没有改写。
        这个站点是静态的，没有后端，所以不做实时调用——但每条都能对着评测集查到。
      </p>

      <div class="demo__grid">
        <section class="demo__input" aria-label="输入">
          <h2>输入</h2>
          <div class="field">
            <span class="field__label">客户原话</span>
            <p class="field__value">{{ active.scene }}</p>
          </div>
          <div class="field">
            <span class="field__label">业务背景</span>
            <p class="field__value">{{ active.background }}</p>
          </div>
          <div class="field">
            <span class="field__label">已知角色</span>
            <p class="field__value">{{ active.roles }}</p>
          </div>

          <h2 class="demo__pick-title">换一条用例</h2>
          <div class="chips">
            <button
              v-for="c in demoCases"
              :key="c.id"
              class="chip"
              :class="{ 'chip--on': c.id === activeId }"
              type="button"
              @click="activeId = c.id"
            >
              <span class="chip__id">{{ c.id }}</span>
              {{ c.label }}
            </button>
          </div>

          <p class="demo__note">
            为什么不实时调用：静态站点没有后端，把 Dify 的 API key 放前端等于公开。
            真实产品里这一步应该走服务端代理。
          </p>
        </section>

        <section class="demo__output" aria-label="输出">
          <div class="out-head">
            <h2>输出</h2>
            <span class="out-tag">原始结果 · {{ active.id }}</span>
          </div>
          <div class="markdown" v-html="html"></div>
        </section>
      </div>

      <p class="demo__foot">
        想看它为什么从 19/30 变成 29/30 ——
        <a href="/work/agent.html">回到案例页看评测记录</a>。
      </p>
    </div>
  </main>
</template>

<style scoped>
.demo { padding: 28px 0 80px; }
.demo__kick {
  font: 600 8pt/1 'Bahnschrift', sans-serif;
  letter-spacing: 0.16em;
  color: var(--muted);
  margin: 26px 0 8px;
}
.demo__title { font-size: clamp(24px, 3.4vw, 38px); margin: 0 0 12px; }
.demo__lead { max-width: 62ch; color: var(--ink-soft); margin: 0 0 28px; }

.demo__grid {
  display: grid;
  grid-template-columns: minmax(260px, 0.72fr) minmax(0, 1.28fr);
  gap: 32px;
  align-items: start;
}
@media (max-width: 900px) {
  .demo__grid { grid-template-columns: 1fr; gap: 24px; }
}

.demo__input {
  position: sticky;
  top: 84px;
  border: 1px solid var(--line);
  padding: 18px 18px 16px;
  background: var(--paper-2);
}
@media (max-width: 900px) {
  .demo__input { position: static; }
}

.demo__input h2 { font-size: 11pt; margin: 0 0 10px; letter-spacing: 0.06em; }
.demo__pick-title { margin-top: 20px !important; }

.field { margin: 0 0 12px; }
.field__label { display: block; font-size: 8.4pt; color: var(--muted); letter-spacing: 0.06em; }
.field__value { margin: 2px 0 0; font-size: 10pt; line-height: 1.5; }

.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 9pt;
  cursor: pointer;
  transition: background 0.18s, color 0.18s, border-color 0.18s;
}
.chip:hover { border-color: var(--ink); }
.chip--on { background: var(--ink); border-color: var(--ink); color: var(--paper); }
.chip__id { font-size: 8pt; opacity: 0.65; }

.demo__note {
  margin: 16px 0 0;
  font-size: 8.6pt;
  line-height: 1.6;
  color: var(--muted);
}

.demo__output {
  border: 1px solid var(--line);
  background: var(--paper-2);
  padding: 18px 22px 26px;
  min-height: 320px;
}
.out-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 8px;
  margin-bottom: 6px;
}
.out-head h2 { font-size: 11pt; margin: 0; letter-spacing: 0.06em; }
.out-tag { font-size: 8pt; color: var(--muted); letter-spacing: 0.06em; }

.markdown :deep(h2) { font-size: 12pt; margin: 18px 0 6px; }
.markdown :deep(h3) { font-size: 10.6pt; margin: 16px 0 5px; }
.markdown :deep(h4) { font-size: 10pt; margin: 14px 0 4px; }
.markdown :deep(p) { margin: 5px 0; font-size: 9.8pt; line-height: 1.68; }
.markdown :deep(ul) { margin: 5px 0; padding-left: 18px; }
.markdown :deep(li) { margin: 3px 0; font-size: 9.8pt; line-height: 1.64; }
.markdown :deep(strong) { font-weight: 700; }
.markdown :deep(code) {
  font-size: 9pt;
  background: rgba(21, 23, 27, 0.06);
  padding: 1px 4px;
  border-radius: 3px;
}
.markdown :deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0 10px;
  font-size: 8.8pt;
}
.markdown :deep(th),
.markdown :deep(td) {
  border: 1px solid var(--line);
  padding: 5px 7px;
  text-align: left;
  vertical-align: top;
}
.markdown :deep(th) { background: rgba(21, 23, 27, 0.045); font-weight: 700; }

.demo__foot {
  margin-top: 30px;
  font-size: 9.4pt;
  color: var(--ink-soft);
}
.demo__foot a { color: inherit; text-decoration: underline; text-underline-offset: 3px; }
</style>
