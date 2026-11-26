# 作品集源码（Vue 3 + Vite）

线上地址：https://shenjunhui.cn

## 技术栈
- Vue 3 `<script setup>` + Vite 6，多页构建（`index.html` + `work/*.html`）
- 纯 CSS 设计变量，无 UI 框架
- 内容驱动：`src/data/cases.js` 存 7 个案例，`getCase(slug)` 渲染
- 简历页与文档预览：`public/resume/`、`public/docs/`（PDF 预渲染成 WebP 页图，避免浏览器内嵌失败）

## 本地运行
```
npm install
npm run dev        # 开发
npm run build      # 产物到 dist/
```

## 目录
| 路径 | 说明 |
|---|---|
| `src/App.vue` / `src/main.js` | 首页 |
| `src/CasePage.vue` / `src/case.js` | 案例页（7 个案例共用一套模板） |
| `src/DemoPage.vue` / `src/demo.js` | 需求拆解 Agent 演示页（真实运行结果回放） |
| `src/data/cases.js` | 全部案例文案与结构 |
| `work/*.html` | 每个案例的 HTML 入口 |
| `public/docs/` | PRD / 评测集 / 运行手册（PDF + WebP 页图） |
| `scripts/` | 构建、导出 PDF、发布脚本 |

## 部署
```
node scripts/deploy-both.mjs --build   # 同时发布到 shenjunhui.cn 与备份域名
```
