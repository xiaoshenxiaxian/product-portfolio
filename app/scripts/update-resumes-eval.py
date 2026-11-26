# -*- coding: utf-8 -*-
"""把 30 条评测（19→29）与运行手册写进两份简历，并修正作品集副标题。"""
import io

D = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理"
BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage"

# ---------- 蓝凌 ----------
p1 = D + r"\沈俊辉-AI管培生-蓝凌-2026.html"
s = io.open(p1, encoding="utf-8").read()

old_b2 = "<li><b>调试出三个问题并修掉：</b>检索阈值过高导致模板召回不到、推理过程混进输出、无匹配模板时整段降级成空话。</li>"
old_b3 = "<li>跑 <b>5 条用例过 4 条</b>；如实标注——单场景、单用户、无权限与审计，离企业级 Agent 平台还差得远，这四样正是想在蓝凌补的。</li>"

new_b2 = "<li><b>建 30 条评测集</b>（7 类场景，含 11 条该失败的），基线 <b>19/30</b>；定位出两类问题：输出格式（推理泄漏、JSON 未解析）与判定过严（该出方案时只提问）。</li>"
new_b3 = "<li>两轮迭代到 <b>29/30</b>；写了 2 页运行手册（坏了怎么修、改版怎么回滚、成本与限流），并如实标注边界：单场景、无权限与审计，离企业级还差得远。</li>"

for old, new in ((old_b2, new_b2), (old_b3, new_b3)):
    if old not in s:
        print("MISS 蓝凌:", old[:20])
    s = s.replace(old, new)
io.open(p1, "w", encoding="utf-8").write(s)
print("蓝凌 ok:", "30 条评测集" in s)

# ---------- 领星 ----------
p2 = D + r"\沈俊辉-产品经理-领星-2026.html"
s2 = io.open(p2, encoding="utf-8").read()

old2 = "<li><b>AI 提效：</b>四节点工作流（输入 → 检索 → 生成 → 输出），把客户一句抱怨拆成角色、流程、异常、字段与验收；知识库 6 篇，<b>5 条用例过 4 条</b>。</li>"
new2 = "<li><b>AI 提效：</b>四节点工作流（输入 → 检索 → 生成 → 输出），把客户一句抱怨拆成角色、流程、异常、字段与验收；知识库 6 篇。</li>"

old3 = "<li><b>调过的坑：</b>检索阈值太高导致模板召回不到、推理过程混进输出、没有匹配模板时整段降级成空话；三个都修了。</li>"
new3 = "<li><b>做了评测：</b>建 30 条评测集（7 类场景），基线 19/30；修掉格式与判定两类问题，两轮迭代到 <b>29/30</b>，并写了可交接的运行手册。</li>"

for old, new in ((old2, new2), (old3, new3)):
    if old not in s2:
        print("MISS 领星:", old[:20])
    s2 = s2.replace(old, new)
io.open(p2, "w", encoding="utf-8").write(s2)
print("领星 ok:", "建 30 条评测集" in s2)

# ---------- 作品集副标题 ----------
p3 = BASE + r"\src\data\cases.js"
s3 = io.open(p3, encoding="utf-8").read()
old_sub = "知识库 6 篇，实测 5 条用例。"
new_sub = "知识库 6 篇；30 条评测集，两轮迭代从 19/30 到 29/30。"
if old_sub in s3:
    s3 = s3.replace(old_sub, new_sub)
    io.open(p3, "w", encoding="utf-8").write(s3)
print("副标题 ok:", "两轮迭代从 19/30" in s3)
