# -*- coding: utf-8 -*-
"""只重新生成分享卡，不动简历与其他素材。"""
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改"
PUBLIC = os.path.join(ROOT, "homepage", "public")

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
print("share.jpg", os.path.getsize(os.path.join(PUBLIC, "share.jpg")), "bytes")
