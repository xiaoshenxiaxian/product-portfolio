# -*- coding: utf-8 -*-
"""去掉案例页顶部重复的「先看它怎么拆（演示）」小节与按钮，只留底部按钮区。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

start = s.index("      {\n        h: '先看它怎么拆（演示）',")
end = s.index("      {\n        h: '为什么做一个「需求拆解」Agent',")
s = s[:start] + s[end:]

io.open(p, "w", encoding="utf-8").write(s)
print("removed:", "先看它怎么拆" not in s, "| demo doc kept:", "agent-demo.html" in s)
