# -*- coding: utf-8 -*-
"""把构建产物打成单文件 HTML（内联 CSS/JS），可离线双击打开或直接发人。"""
import io
import os
import re

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage"
DIST = BASE + r"\dist"
SRC = DIST + r"\work\agent-demo.html"
OUT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-需求拆解Agent-演示.html"

html = io.open(SRC, encoding="utf-8").read()

# 内联 CSS
def inline_css(m):
    href = m.group(1)
    path = os.path.join(DIST, href.lstrip("/").replace("/", os.sep))
    if not os.path.exists(path):
        return m.group(0)
    css = io.open(path, encoding="utf-8").read()
    return f"<style>\n{css}\n</style>"

html = re.sub(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"[^>]*>', inline_css, html)

# 内联 JS（模块）
def inline_js(m):
    src = m.group(1)
    path = os.path.join(DIST, src.lstrip("/").replace("/", os.sep))
    if not os.path.exists(path):
        return m.group(0)
    js = io.open(path, encoding="utf-8").read()
    return f"<script type=\"module\">\n{js}\n</script>"

html = re.sub(r'<script[^>]+type="module"[^>]+src="([^"]+)"[^>]*></script>', inline_js, html)

# 去掉 modulepreload（已内联）
html = re.sub(r'<link[^>]+rel="modulepreload"[^>]*>', "", html)

# 相对根路径的图片等：本页没有图片，保留即可
io.open(OUT, "w", encoding="utf-8").write(html)

remain = re.findall(r'/assets/[A-Za-z0-9._-]+', html)
print("saved", OUT)
print("size KB:", round(os.path.getsize(OUT) / 1024))
print("未内联的 assets 引用:", remain[:5] if remain else "无")
