# -*- coding: utf-8 -*-
"""接入演示页：vite 入口 + Agent 案例加按钮 + 案例页顶部提示。"""
import io

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage"

# 1) vite 入口
vp = BASE + r"\vite.config.js"
v = io.open(vp, encoding="utf-8").read()
if "work/agent-demo.html" not in v:
    v = v.replace(
        "        agent: resolve(import.meta.dirname, 'work/agent.html'),",
        "        agent: resolve(import.meta.dirname, 'work/agent.html'),\n        'agent-demo': resolve(import.meta.dirname, 'work/agent-demo.html'),",
    )
    io.open(vp, "w", encoding="utf-8").write(v)
print("vite:", "agent-demo" in io.open(vp, encoding="utf-8").read())

# 2) 案例数据：docs 里加演示按钮 + 第一节前加一句引导
p = BASE + r"\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

if "agent-demo.html" not in s:
    s = s.replace(
        "      { label: '查看 PRD 摘要（2 页）', href: '/docs/view.html?f=agent-prd' },",
        "      { label: '打开演示（6 条真实用例）', href: '/work/agent-demo.html' },\n"
        "      { label: '查看 PRD 摘要（2 页）', href: '/docs/view.html?f=agent-prd' },",
    )

# 在「为什么做一个」小节前插一句「先看演示」
demo_para = """      {
        h: '先看它怎么拆（演示）',
        paras: [
          '打开演示页，选一条输入就能看到它 2026-11-25 跑出来的原样结果——包括该提问的时候只提问、该拒绝的时候直接拒绝。',
        ],
        links: [{ label: '打开演示', href: '/work/agent-demo.html' }],
      },
"""
if "先看它怎么拆（演示）" not in s:
    s = s.replace("      {\n        h: '为什么做一个「需求拆解」Agent',", demo_para + "      {\n        h: '为什么做一个「需求拆解」Agent',")

io.open(p, "w", encoding="utf-8").write(s)
print("demo button:", "agent-demo.html" in s)
