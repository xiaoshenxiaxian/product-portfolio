# -*- coding: utf-8 -*-
"""修正蓝凌版第二条子弹（上一条替换锚点不匹配）。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI管培生-蓝凌-2026.html"
s = io.open(p, encoding="utf-8").read()

old = "<li>调试出三个问题并修掉：检索阈值过高导致模板召回不到、推理过程混进输出、无匹配模板时整段降级成空话。</li>"
new = "<li><b>建 30 条评测集</b>（7 类场景，含 11 条该失败的），基线 <b>19/30</b>；定位出两类问题：输出格式（推理泄漏、JSON 未解析）与判定过严（该出方案时只提问）。</li>"

if old in s:
    s = s.replace(old, new)
    io.open(p, "w", encoding="utf-8").write(s)
    print("fixed")
else:
    print("MISS")
