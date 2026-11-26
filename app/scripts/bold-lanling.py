# -*- coding: utf-8 -*-
"""只调加粗：标签还原，加粗「所有权 + 数字」。"""
import io

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI管培生-蓝凌-2026.html"
s = io.open(path, encoding="utf-8").read()
before = s.count("<b>")

pairs = [
    # 标签取消加粗
    ("<b>算清每一笔账：</b>", "算清每一笔账："),
    ("<b>拆开看客人：</b>", "拆开看客人："),
    ("<b>参与需求梳理：</b>", "参与需求梳理："),
    ("<b>跟到联调：</b>", "跟到联调："),
    # 所有权单独加粗
    ("<b>独立撰写 PRD：</b>", "<b>独立撰写</b> PRD："),
    # 唯一验证过的结果加粗
    ("跑 5 条用例过 4 条；", "跑 <b>5 条用例过 4 条</b>；"),
]

for a, b in pairs:
    if a not in s:
        print("MISS:", a[:22])
    s = s.replace(a, b)

io.open(path, "w", encoding="utf-8").write(s)
print("bold count:", before, "->", s.count("<b>"))
