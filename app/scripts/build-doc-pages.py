# -*- coding: utf-8 -*-
"""把 /docs 下的 PDF 逐页转成 WebP，并生成 manifest.json。

依赖：先用 LibreOffice Kit 把 PDF 渲染成 PNG 到临时目录（由外部命令完成），
本脚本负责把 PNG 压成 WebP 并写 manifest。
"""
import io
import json
import os
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

DOCS = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\public\docs"

# slug -> (标题, 页数)
META = {
    "huoliyuan-order-prd": "订单管理与支付实名认证模块 · PRD",
    "order-help-center": "住宿订单帮助中心",
    "guanjing-prd": "观境文旅 · 景区／博物馆小程序 PRD",
    "zhuaban-prd": "爪伴 · 同城宠物领养管理系统 PRD",
    "zhilan-prd": "知澜 · 在线教育平台 PRD",
    "desktop-prd": "桌面美化 · 付费墙 PRD 摘要",
    "yuexi-prd": "月汐 · 树洞 PRD 摘要",
    "agent-prd": "需求拆解 Agent · PRD 摘要",
}

render_root = sys.argv[1] if len(sys.argv) > 1 else ""
manifest = {}

for slug, title in META.items():
    src_dir = os.path.join(render_root, slug)
    if not os.path.isdir(src_dir):
        print("MISSING RENDER", slug)
        continue
    out_dir = os.path.join(DOCS, "pages", slug)
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(f for f in os.listdir(src_dir) if f.lower().endswith(".png"))
    count = 0
    for name in files:
        img = Image.open(os.path.join(src_dir, name)).convert("RGB")
        if img.width > 980:
            h = round(img.height * 980 / img.width)
            img = img.resize((980, h), Image.LANCZOS)
        count += 1
        img.save(os.path.join(out_dir, f"{count:02d}.webp"), "WEBP", quality=80, method=6)
    manifest[slug] = {"title": title, "pages": count, "pdf": f"{slug}.pdf"}
    print(slug, count, "pages")

io.open(os.path.join(DOCS, "manifest.json"), "w", encoding="utf-8").write(
    json.dumps({"docs": manifest}, ensure_ascii=False, indent=2)
)
print("manifest written")
