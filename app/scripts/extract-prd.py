# -*- coding: utf-8 -*-
"""提取 PDF 文本并输出指定页的节选（控制台按 UTF-8 输出）。"""
import sys

from pypdf import PdfReader

sys.stdout.reconfigure(encoding="utf-8")

src = sys.argv[1]
pages = sys.argv[2] if len(sys.argv) > 2 else "head"
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 260

reader = PdfReader(src)
print("PAGES", len(reader.pages))

if pages == "head":
    for i, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").replace("\n", " ")
        print(f"[{i}] {text[:limit]}")
else:
    for spec in pages.split(","):
        i = int(spec)
        page = reader.pages[i - 1]
        print(f"===== PAGE {i} =====")
        print(page.extract_text() or "")
