# -*- coding: utf-8 -*-
"""合并成本两行、删除重复占位行。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-需求拆解Agent-运行手册.html"
s = io.open(p, encoding="utf-8").read()

s = s.replace(
    '<tr><td>调用成本</td><td>单次约 3–4 万 tokens（含检索上下文）；<b>缓存命中占 99.6%</b>，实际计费很低</td></tr>\n'
    '          <tr><td>实测消耗</td><td>2026-11-25 当日 1.128 亿 tokens（命中 1.124 亿 / 未命中 21 万 / 输出 22 万）</td></tr>',
    '<tr><td>调用成本</td><td>单次约 3–4 万 tokens（缓存命中 99.6%）；2026-11-25 当日 1.128 亿 tokens，实际计费很低</td></tr>',
)

# 删掉残留的重复占位行
import re
s = re.sub(r'\s*<tr><td>模型成本</td><td>\[[^\]]*\]</td></tr>', "", s)

io.open(p, "w", encoding="utf-8").write(s)
print("dup removed:", "模型成本" not in s, "| rows:", s.count("<tr><td>"))
