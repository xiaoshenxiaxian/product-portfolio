# -*- coding: utf-8 -*-
"""从素版生成「AI 产品经理（快付·厦门）」版。"""
import io
import shutil

D = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理"
src = D + r"\沈俊辉-产品助理-素版-2026.html"
dst = D + r"\沈俊辉-AI产品经理-快付-2026.html"

shutil.copyfile(src, dst)
s = io.open(dst, encoding="utf-8").read()

# 标题 / 求职意向 / 城市
s = s.replace("<title>沈俊辉 · 产品助理 · 2026</title>", "<title>沈俊辉 · AI 产品经理 · 2026</title>")
s = s.replace("求职意向：产品助理", "求职意向：AI 产品经理")
s = s.replace("深圳 / 广州 / 杭州 · 可即时到岗", "厦门 / 深圳 · 可即时到岗")

# 摘要：把「判断 + 评测」提到最前
old_sum = "3 个月产品助理实习 + 3 个项目：把积压的 20 多个问题单关掉 <b>17 个</b>；自己做的项目里，先找 12 个人来点，再把主链路从 5 步砍到 3 步。习惯先问「谁在什么情况下会卡住」，再动手。"
new_sum = "做完过一件事：判断一个 AI 需求该用工作流还是 Agent，再建 <b>30 条评测集</b>把它从 19/30 做到 <b>29/30</b>；也写过订单后台的 8 页 PRD 和客服用的帮助中心。习惯先问「谁在什么情况下会卡住」，再动手。"
if old_sum in s:
    s = s.replace(old_sum, new_sum)
else:
    print("MISS summary")

# 技能：AI 与工作流置顶，拆成三行
old_skills = """        <p><b>需求与文档：</b>需求收集与澄清、PRD、流程图、状态机、字段表、验收标准、异常分支；跟 UI / 研发 / 测试对齐、联调与验收</p>
        <p><b>原型 / 数据 / AI：</b>可点 HTML 原型（手机 / 电脑双版式）、Axure、Figma、SQL；Dify 工作流与评测集设计，能判断一个需求该用工作流还是 Agent</p>"""
new_skills = """        <p><b>AI 与工作流：</b>Dify（工作流、知识库、提示词调优）、评测集设计与失败归因；能判断一个需求该用工作流还是 Agent</p>
        <p><b>需求与文档：</b>需求收集与澄清、PRD、流程图、状态机、字段表、验收标准、异常分支；跟研发 / 测试对齐、联调与验收</p>
        <p><b>原型与数据：</b>可点 HTML 原型、Axure、Figma；SQL 查数、Excel 分类统计；能把指标说清「怎么算」</p>"""
if old_skills in s:
    s = s.replace(old_skills, new_skills)
else:
    print("MISS skills")

io.open(dst, "w", encoding="utf-8").write(s)
print("saved", dst)
