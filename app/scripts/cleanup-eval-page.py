# -*- coding: utf-8 -*-
"""收尾：删除独立评测页与 vite 入口，微调措辞。"""
import io
import os

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage"

# 1) 删除页面
page = BASE + r"\work\agent-eval.html"
if os.path.exists(page):
    os.remove(page)
    print("removed page")

# 2) vite 入口
vp = BASE + r"\vite.config.js"
v = io.open(vp, encoding="utf-8").read()
v = v.replace("        'agent-eval': resolve(import.meta.dirname, 'work/agent-eval.html'),\n", "")
io.open(vp, "w", encoding="utf-8").write(v)
print("vite cleaned:", "agent-eval" not in v)

# 3) 措辞
p = BASE + r"\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()
s = s.replace("这个页面记录完整过程——包括没改好的那一轮。", "下面几节记录完整过程——包括没改好的那一轮。")
io.open(p, "w", encoding="utf-8").write(s)
print("wording ok:", "下面几节记录完整过程" in s)
