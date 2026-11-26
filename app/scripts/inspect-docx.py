# -*- coding: utf-8 -*-
"""检查 docx 内容：段落、表格、可疑占位符。"""
import re
import sys

from docx import Document

sys.stdout.reconfigure(encoding="utf-8")

path = sys.argv[1]
doc = Document(path)

print("== 段落数:", len(doc.paragraphs), " 表格数:", len(doc.tables))
print("\n== 前 40 段 ==")
for i, p in enumerate(doc.paragraphs[:40]):
    t = p.text.strip()
    if t:
        print(f"[{i}] ({p.style.name}) {t[:110]}")

print("\n== 表格首行 ==")
for i, table in enumerate(doc.tables, 1):
    head = " | ".join(c.text.strip()[:14] for c in table.rows[0].cells)
    print(f"T{i} ({len(table.rows)}x{len(table.columns)}): {head}")

print("\n== 可疑内容 ==")
all_text = "\n".join(p.text for p in doc.paragraphs)
for table in doc.tables:
    for row in table.rows:
        all_text += "\n" + " | ".join(c.text for c in row.cells)

patterns = ["TODO", "XXX", "xx", "待补", "待定", "见图", "下图", "略", "（略）", "PS", "注：", "如图"]
for pat in patterns:
    hits = [m.start() for m in re.finditer(pat, all_text)]
    if hits:
        print(f"'{pat}' x{len(hits)}")

for kw in ["同城宠物领养", "爪伴", "宠物"]:
    print(f"'{kw}' 出现 {all_text.count(kw)} 次")
