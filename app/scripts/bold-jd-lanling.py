# -*- coding: utf-8 -*-
"""按 JD 关键词加粗：需求梳理 / 独立撰写 PRD / 联调 / 状态 / 工作流 / 用例结果。"""
import io

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI管培生-蓝凌-2026.html"
s = io.open(path, encoding="utf-8").read()
before = s.count("<b>")

pairs = [
    # 实习1：JD「需求拆解」
    ("参与需求梳理：", "参与<b>需求梳理</b>："),
    # 实习2：JD「方案设计 / 文档」+ 所有权
    ("<b>独立撰写</b> PRD：", "<b>独立撰写 PRD</b>："),
    # 实习3：JD「上线调优 / 交付实现」
    ("跟到联调：", "跟到<b>联调</b>："),
    # Agent：JD「Agent 工具链」
    ("用 Dify 搭四节点工作流", "用 Dify 搭<b>四节点工作流</b>"),
]

for a, b in pairs:
    if a not in s:
        print("MISS:", a[:22])
    s = s.replace(a, b)

io.open(path, "w", encoding="utf-8").write(s)
print("bold:", before, "->", s.count("<b>"))
