# -*- coding: utf-8 -*-
"""把旧案例页的正文抽成精简摘要，供新详情页复用。"""
import html
import os
import re

ROOT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\portfolio-2026"
FILES = [
    "work-huoliyuan.html",
    "work-yuesi.html",
    "work-zhuaban.html",
    "work-zhilan.html",
    "work-guanying.html",
    "work-desktop-app.html",
]
OUT = os.path.join(os.environ.get("TEMP", "."), "case-digest.md")


def strip_tags(fragment):
    fragment = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    fragment = re.sub(r"<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"</(p|h1|h2|h3|li|tr|div)>", "\n", fragment)
    fragment = re.sub(r"</t[dh]>", " | ", fragment)
    text = re.sub(r"<[^>]+>", "", fragment)
    text = html.unescape(text)
    lines = [l.strip(" \t|") for l in text.split("\n")]
    return [l for l in lines if l]


chunks = []
for name in FILES:
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        chunks.append(f"## {name} (missing)")
        continue
    src = open(path, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", src, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", src, re.S)
    sub = re.search(r'class="case-sub"[^>]*>(.*?)</p>', src, re.S)
    meta = re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", src, re.S)
    body = re.search(r"<article class=\"case-body\">(.*?)</article>", src, re.S)
    note = re.search(r'class="note"[^>]*>(.*?)</p>', src, re.S)

    chunks.append(f"## {name}")
    chunks.append("title: " + (strip_tags(title.group(1))[0] if title else ""))
    if h1:
        chunks.append("h1: " + " ".join(strip_tags(h1.group(1))))
    if sub:
        chunks.append("sub: " + " ".join(strip_tags(sub.group(1))))
    if meta:
        chunks.append("meta: " + "; ".join(f"{k}={strip_tags(v)[0] if strip_tags(v) else ''}" for k, v in meta))
    if body:
        for line in strip_tags(body.group(1)):
            chunks.append(line)
    if note:
        chunks.append("note: " + " ".join(strip_tags(note.group(1))))
    chunks.append("")

open(OUT, "w", encoding="utf-8").write("\n".join(chunks))
print("wrote", OUT, len(chunks), "lines")
