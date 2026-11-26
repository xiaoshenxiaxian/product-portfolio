# -*- coding: utf-8 -*-
"""把蓝凌版摘要压成两行。"""
import io
import re

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI管培生-蓝凌-2026.html"
s = io.open(path, encoding="utf-8").read()

new = (
    '<p class="summary">\n'
    "        计算机 2026 届。写过订单支付后台的 <b>8 页 PRD</b>（6 状态、权限、验收），跟研发联调到集成测试；"
    "也用 Dify 搭了能把客户一句话拆成流程和字段的 <b>Agent</b>（5 条用例 4 条通过）。\n"
    "      </p>"
)

s2 = re.sub(r'<p class="summary">[\s\S]*?</p>', new, s, count=1)
io.open(path, "w", encoding="utf-8").write(s2)
print("changed:", s2 != s)
print("has 门店 in summary:", "门店站过" in s2)
