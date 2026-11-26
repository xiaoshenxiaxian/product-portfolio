# -*- coding: utf-8 -*-
"""文档标签从「下载」改为「查看」。"""
import io

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(path, encoding="utf-8").read()

pairs = [
    ("label: '脱敏 PRD（PDF，8 页）'", "label: '查看脱敏 PRD（8 页）'"),
    ("label: '订单帮助中心（PDF，3 页）'", "label: '查看帮助中心（3 页）'"),
    ("label: 'PRD 摘要（PDF，2 页）'", "label: '查看 PRD 摘要（2 页）'"),
    ("label: '完整 PRD（PDF，12 页）'", "label: '查看完整 PRD（12 页）'"),
    ("label: '完整 PRD（PDF，16 页）'", "label: '查看完整 PRD（16 页）'"),
    ("label: '付费墙 PRD 摘要（PDF，2 页）'", "label: '查看付费墙 PRD 摘要（2 页）'"),
]
for a, b in pairs:
    s = s.replace(a, b)

io.open(path, "w", encoding="utf-8").write(s)
print("still has PDF label:", "（PDF，" in s)
