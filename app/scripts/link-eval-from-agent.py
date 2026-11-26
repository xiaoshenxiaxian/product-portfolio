# -*- coding: utf-8 -*-
"""在 Agent 案例页加一个「评测记录」入口。"""
import io
import re

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

anchor = "        { label: 'PRD 摘要（2 页）', href: '/docs/view.html?f=agent-prd' },"
if anchor not in s:
    print("MISS anchor")
else:
    if "评测记录（19/30" not in s:
        s = s.replace(
            anchor,
            anchor + "\n        { label: '评测记录（19/30 → 29/30）', href: '/work/agent-eval.html' },",
        )
    io.open(p, "w", encoding="utf-8").write(s)

print("ok:", "评测记录（19/30" in s)
