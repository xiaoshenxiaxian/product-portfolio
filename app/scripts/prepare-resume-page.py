# -*- coding: utf-8 -*-
"""把简历 HTML + 图片发布成站内可预览页面 /resume/。

图片统一转 WebP 并缩到合适宽度，避免首访时照片、截图为空白。
"""
import os
import shutil

from PIL import Image

SRC = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\月汐-树洞\简历"
DST = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\public\resume"

# 原文件 -> (新文件名, 目标宽度)
IMAGES = {
    "photo.jpg": ("photo.webp", 620),
    "s1.png": ("s1.webp", 620),
    "s2.png": ("s2.webp", 620),
    "s3.png": ("s3.webp", 620),
    "qr.png": ("qr.png", 660),
}

BAR = """
<div class="rv-bar">
  <a href="/">← 返回作品集</a>
  <a class="rv-dl" href="/resume.pdf">下载 PDF</a>
</div>
<style>
  .rv-bar {
    position: fixed;
    right: 18px;
    bottom: 18px;
    z-index: 99;
    display: flex;
    gap: 8px;
    font: 500 12.5px/1 "Noto Sans SC", "PingFang SC", system-ui, sans-serif;
    letter-spacing: .04em;
  }
  .rv-bar a {
    padding: 10px 16px;
    border: 1px solid rgba(21, 23, 27, .22);
    border-radius: 999px;
    background: #F7F4ED;
    color: #15171B;
    text-decoration: none;
    transition: background .2s, color .2s, border-color .2s;
  }
  .rv-bar a:hover { background: #15171B; border-color: #15171B; color: #F7F4ED; }
  .rv-dl { border-color: rgba(21, 23, 27, .45); }
  @media print { .rv-bar { display: none } }

  /* 手机上看整页：按视口缩放 A4，避免只露出左半边 */
  @media (max-width: 900px) { .page { zoom: 0.66 } }
  @media (max-width: 640px) { .page { zoom: 0.48 } }
  @media (max-width: 420px) { .page { zoom: 0.43 } }
</style>
"""


def convert(src_name, dst_name, width):
    src = os.path.join(SRC, "assets", src_name)
    dst = os.path.join(DST, "assets", dst_name)
    if not os.path.exists(src):
        print("missing", src_name)
        return
    img = Image.open(src)
    if img.width > width:
        height = round(img.height * width / img.width)
        img = img.resize((width, height), Image.LANCZOS)
    if dst_name.endswith(".webp"):
        img.convert("RGB").save(dst, "WEBP", quality=82, method=6)
    else:
        img.save(dst)
    print("  ", dst_name, img.size, round(os.path.getsize(dst) / 1024, 1), "KB")


def main():
    assets_dir = os.path.join(DST, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    for old in os.listdir(assets_dir):
        os.remove(os.path.join(assets_dir, old))

    for src_name, (dst_name, width) in IMAGES.items():
        convert(src_name, dst_name, width)

    html = open(os.path.join(SRC, "沈俊辉-产品经理-月汐-简历.html"), encoding="utf-8").read()
    for src_name, (dst_name, _) in IMAGES.items():
        html = html.replace(f"assets/{src_name}", f"assets/{dst_name}")

    if "</body>" not in html:
        raise SystemExit("no </body>")
    html = html.replace("</body>", BAR + "</body>", 1)
    open(os.path.join(DST, "index.html"), "w", encoding="utf-8").write(html)
    print("resume page written")


main()
