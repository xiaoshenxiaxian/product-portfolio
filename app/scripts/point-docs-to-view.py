# -*- coding: utf-8 -*-
"""把案例页的 PRD 链接从 PDF 直链改成站内预览页。"""
import io
import re

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(path, encoding="utf-8").read()

s = re.sub(r"href: '/docs/([a-z-]+)\.pdf'", lambda m: "href: '/docs/view.html?f=" + m.group(1) + "'", s)

s = s.replace(
    "{ label: '下载脱敏 PRD（PDF，8 页）', href: '/docs/view.html?f=huoliyuan-order-prd' }",
    "{ label: '查看脱敏 PRD（8 页）', href: '/docs/view.html?f=huoliyuan-order-prd', download: false }",
)

io.open(path, "w", encoding="utf-8").write(s)
print("pdf direct links left:", len(re.findall(r"/docs/[a-z-]+\.pdf", s)))
print("view links:", len(re.findall(r"/docs/view\.html\?f=", s)))
