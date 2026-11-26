# -*- coding: utf-8 -*-
"""把 dist-single 的构建产物内联成一个 HTML 文件。"""
import io
import os
import re

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage"
DIST = BASE + r"\dist-single"
SRC = DIST + r"\work\agent-demo.html"
OUT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-需求拆解Agent-演示.html"

html = io.open(SRC, encoding="utf-8").read()


def read_asset(href):
    path = os.path.join(DIST, href.lstrip("/").replace("/", os.sep))
    return io.open(path, encoding="utf-8").read() if os.path.exists(path) else None


def inline_css(m):
    css = read_asset(m.group(1))
    return f"<style>\n{css}\n</style>" if css else m.group(0)


def inline_js(m):
    js = read_asset(m.group(1))
    return f'<script type="module">\n{js}\n</script>' if js else m.group(0)


html = re.sub(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"[^>]*>', inline_css, html)
html = re.sub(r'<script[^>]+type="module"[^>]+src="([^"]+)"[^>]*></script>', inline_js, html)
html = re.sub(r'<link[^>]+rel="modulepreload"[^>]*>', "", html)

io.open(OUT, "w", encoding="utf-8").write(html)
print("saved", OUT)
print("KB:", round(os.path.getsize(OUT) / 1024))
print("remaining refs:", re.findall(r'/assets/[A-Za-z0-9._-]+', html) or "无")
print("has createApp:", "createApp" in html)
