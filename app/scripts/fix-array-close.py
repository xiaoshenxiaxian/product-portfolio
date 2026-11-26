# -*- coding: utf-8 -*-
"""修复 agent sections 数组闭合位置错误。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

marker = "    ],\n      {\n        h: '为什么给一个 Agent 做评测'"
start = s.index(marker)
gal = s.index("\n    gallery: [", start)

block = s[start:gal]                     # 从错误的 ], 到 gallery 之前
body = block.replace("    ],\n", "", 1)  # 去掉提前闭合
new = body.rstrip() + "\n    ],"         # 在最后补上闭合

s = s[:start] + new + s[gal:]
io.open(p, "w", encoding="utf-8").write(s)
print("patched")
