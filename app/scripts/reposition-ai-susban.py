# -*- coding: utf-8 -*-
"""素版：把 AI 项目从「我搭了」改成「我判断 + 我验收」。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品助理-素版-2026.html"
s = io.open(p, encoding="utf-8").read()
before = s

# 1) Agent 两条 → 三条（判断 / 评测 / 兜底）
old_agent = """          <li><b>问题：</b>客户一句「订单状态查不到」，要拆成流程、角色、字段和验收，每次都从头来一遍。</li>
          <li><b>动作与结果：</b>搭四节点工作流（输入 → 检索 → 生成 → 输出），知识库 6 篇；建 <b>30 条评测集</b>，基线 19/30，两轮改到 <b>29/30</b>，另写 2 页运行手册。</li>"""
new_agent = """          <li><b>判断：</b>这个场景选了<b>工作流而不是 Agent</b>——自由 Agent 同一输入两次结果不同，就没法做对比评测。</li>
          <li><b>评测：</b>建 <b>30 条评测集</b>（含 11 条「该失败」的），基线 19/30；修掉输出格式与判定过严两类问题，两轮改到 <b>29/30</b>。</li>
          <li><b>兜底：</b>写 2 页运行手册（坏了怎么修、改版怎么回滚、成本与限流），边界写明「单场景、无权限与审计」。</li>"""

if old_agent in s:
    s = s.replace(old_agent, new_agent)
else:
    print("MISS agent")

# 2) 桌面美化两条并成一条，腾出空间
old_desktop = """          <li><b>问题：</b>一款 4.74 分的 App，最近 50 条评论只有 <b>3.52</b>；把 50 条差评逐条分类，再对比 3 个竞品的收费方式，定位到主因是广告太频、弹窗时机不对。</li>
          <li><b>动作与结果：</b>输出 <b>10 个问题、3 个改法</b>；第一个改法做成 6 个状态的可点原型，诊断和原型已上线。</li>"""
new_desktop = """          <li><b>动作与结果：</b>一款 4.74 分的 App，最近 50 条评论只有 <b>3.52</b>——把 50 条差评逐条分类、对比 3 个竞品收费方式，定位到主因是广告太频、弹窗时机不对；输出 <b>10 个问题、3 个改法</b>，第一个做成 6 个状态的可点原型。</li>"""

if old_desktop in s:
    s = s.replace(old_desktop, new_desktop)
else:
    print("MISS desktop")

# 3) 技能行：把「会用工具」换成「会判断与验收」
s = s.replace(
    "<b>原型 / 数据 / AI：</b>可点 HTML 原型（手机 / 电脑双版本）、Axure、Figma、评论归因、SQL、用 AI 出初稿并核验",
    "<b>原型 / 数据 / AI：</b>可点 HTML 原型（手机 / 电脑双版本）、Axure、Figma、SQL；Dify 工作流与评测集设计，能判断一个需求该用工作流还是 Agent",
)

io.open(p, "w", encoding="utf-8").write(s)
print("changed:", s != before)
