# -*- coding: utf-8 -*-
"""素版简历：Agent 条目改为「原型 · 单场景 · 个人自测」，结果换成 30 条评测 19→29。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品助理-素版-2026.html"
s = io.open(p, encoding="utf-8").read()
before = s

s = s.replace(
    '<span>需求拆解 Agent ｜ <span class="role">Dify 工作流 + 知识库 · 个人项目</span></span>',
    '<span>需求拆解 Agent 原型 ｜ <span class="role">Dify 工作流 + 知识库 · 单场景 · 个人自测</span></span>',
)

s = s.replace(
    "<li><b>动作与结果：</b>搭四节点工作流（用户输入 → 知识检索 → LLM → 输出），知识库 <b>6 篇</b>用自己的 PRD 与两个真实案例；实测 <b>5 条用例 4 条通过</b>，修掉检索阈值、推理标签混入、缺模板降级三个问题。</li>",
    "<li><b>动作与结果：</b>搭四节点工作流（输入 → 检索 → 生成 → 输出），知识库 <b>6 篇</b>；建 <b>30 条评测集</b>，基线 19/30，两轮迭代到 <b>29/30</b>，并写 2 页运行手册。</li>",
)

io.open(p, "w", encoding="utf-8").write(s)
print("changed:", s != before, "| 30 条:", "30 条评测集" in s)
