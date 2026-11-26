# -*- coding: utf-8 -*-
"""把真实原型截图转成网页资源，并生成分享图与简历副本。"""
import os
import shutil

from PIL import Image, ImageDraw, ImageFont

ROOT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改"
WORKSPACE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改"
SRC = os.path.join(ROOT, "portfolio", "assets")
DESK = os.path.join(WORKSPACE, "桌面美化App-交互原型-2026")
PUBLIC = os.path.join(ROOT, "homepage", "public")
OUT = os.path.join(PUBLIC, "work")

os.makedirs(OUT, exist_ok=True)

jobs = [
    (os.path.join(SRC, "moontide", "01.png"), "moontide-1.webp"),
    (os.path.join(SRC, "moontide", "02.png"), "moontide-2.webp"),
    (os.path.join(SRC, "moontide", "03.png"), "moontide-3.webp"),
    (os.path.join(SRC, "moontide", "04.png"), "moontide-4.webp"),
    (os.path.join(SRC, "pawbei", "01.png"), "pawbei-1.webp"),
    (os.path.join(SRC, "pawbei", "03.png"), "pawbei-3.webp"),
    (os.path.join(SRC, "pawbei", "05.png"), "pawbei-5.webp"),
    (os.path.join(SRC, "zhilan", "01.png"), "zhilan-1.webp"),
    (os.path.join(SRC, "zhilan", "03.png"), "zhilan-3.webp"),
    (os.path.join(SRC, "zhilan", "05.png"), "zhilan-5.webp"),
    (os.path.join(SRC, "guanying", "01.png"), "guanying-1.webp"),
    (os.path.join(SRC, "guanying", "03.png"), "guanying-3.webp"),
    (os.path.join(SRC, "guanying", "05.png"), "guanying-5.webp"),
    (os.path.join(DESK, "1-浏览-无浮层.png"), "desktop-1.webp"),
    (os.path.join(DESK, "3-AI-输入.png"), "desktop-3.webp"),
    (os.path.join(DESK, "6-订阅-三档试用.png"), "desktop-6.webp"),
]

total = 0
for src, name in jobs:
    if not os.path.exists(src):
        print("MISSING", src)
        continue
    img = Image.open(src).convert("RGB")
    dst = os.path.join(OUT, name)
    img.save(dst, "WEBP", quality=82, method=6)
    size = os.path.getsize(dst)
    total += size
    print("WROTE %-20s %5d x %-5d %6.1f KB" % (name, img.width, img.height, size / 1024))

# 分享图 1200x630
share = Image.new("RGB", (1200, 630), "#E8E5DE")
draw = ImageDraw.Draw(share)
try:
    serif = ImageFont.truetype(r"C:\Windows\Fonts\NotoSerifSC-VF.ttf", 84)
    sans = ImageFont.truetype(r"C:\Windows\Fonts\NotoSansSC-VF.ttf", 28)
except Exception as exc:  # noqa: BLE001
    print("FONT FALLBACK", exc)
    serif = ImageFont.load_default()
    sans = ImageFont.load_default()

draw.text((88, 150), "把模糊的需求，", font=serif, fill="#15171B")
draw.text((88, 262), "做成能点的原型。", font=serif, fill="#15171B")
draw.line((90, 400, 420, 400), fill="#12463C", width=4)
draw.text((90, 432), "沈俊辉 · 产品助理", font=sans, fill="#33373F")
share.save(os.path.join(PUBLIC, "share.jpg"), "JPEG", quality=88)

# 简历 PDF 由 scripts/prepare-resume-page.py + scripts/print-pdf.mjs 生成，
# 这里不再覆盖 public/resume.pdf，避免把新简历回退成旧版。

print("TOTAL %.1f KB in %s" % (total / 1024, OUT))
