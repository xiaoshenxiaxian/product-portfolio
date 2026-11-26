# -*- coding: utf-8 -*-
"""列出指定目录下所有 PDF 的页数与大小。"""
import os
import sys

from pypdf import PdfReader

sys.stdout.reconfigure(encoding="utf-8")

for folder in sys.argv[1:]:
    print("##", folder)
    for name in sorted(os.listdir(folder)):
        if not name.lower().endswith(".pdf"):
            continue
        path = os.path.join(folder, name)
        try:
            pages = len(PdfReader(path).pages)
        except Exception:
            pages = "?"
        kb = round(os.path.getsize(path) / 1024)
        print(f"{pages}\t{kb}KB\t{name}")
