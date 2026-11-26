# -*- coding: utf-8 -*-
"""实习案例素材：封面、PRD 四页、脱敏 PRD 文件。"""
import os
import shutil

from PIL import Image

ROOT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改"
WORKSPACE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改"
P2026 = os.path.join(WORKSPACE, "portfolio-2026", "assets")
PUBLIC = os.path.join(ROOT, "homepage", "public")
WORK = os.path.join(PUBLIC, "work")
DOCS = os.path.join(PUBLIC, "docs")
PRD_PAGES = os.path.join(os.environ.get("TEMP", ""), "prd-render")

os.makedirs(WORK, exist_ok=True)
os.makedirs(DOCS, exist_ok=True)

# 封面
cover = os.path.join(P2026, "img", "cover-huoliyuan.jpg")
if os.path.exists(cover):
    img = Image.open(cover).convert("RGB")
    img.save(os.path.join(WORK, "huoliyuan-cover.webp"), "WEBP", quality=84, method=6)
    print("cover", img.size)
else:
    print("MISSING cover", cover)

# PRD 四页
for i in range(1, 5):
    src = os.path.join(PRD_PAGES, f"page-{i:04d}.png")
    if not os.path.exists(src):
        print("MISSING prd page", src)
        continue
    img = Image.open(src).convert("RGB")
    dst = os.path.join(WORK, f"prd-{i}.webp")
    img.save(dst, "WEBP", quality=80, method=6)
    print("prd", i, img.size, round(os.path.getsize(dst) / 1024, 1), "KB")

# 脱敏 PRD
pdf = os.path.join(P2026, "docs", "huoliyuan-order-prd.pdf")
if os.path.exists(pdf):
    shutil.copyfile(pdf, os.path.join(DOCS, "huoliyuan-order-prd.pdf"))
    print("pdf", round(os.path.getsize(pdf) / 1024, 1), "KB")
else:
    print("MISSING pdf", pdf)
