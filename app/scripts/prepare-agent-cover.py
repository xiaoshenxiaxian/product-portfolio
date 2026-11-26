# -*- coding: utf-8 -*-
"""生成弧线封面（360x779，在页面上会缩到约 140px 宽）。"""
import os

from PIL import Image, ImageDraw, ImageFont

OUT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\public\work"

W, H = 360, 779
cover = Image.new("RGB", (W, H), "#14161A")
draw = ImageDraw.Draw(cover)

serif = ImageFont.truetype(r"C:\Windows\Fonts\NotoSerifSC-VF.ttf", 52)
sans = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 17)
label = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 18)
mono = ImageFont.truetype(r"C:\Windows\Fonts\Bahnschrift.ttf", 14)

draw.text((34, 44), "AGENT 2026", font=mono, fill="#7C838D")
draw.text((34, 92), "需求拆解", font=serif, fill="#E9E6DF")
draw.text((34, 162), "一句话进去，流程出来", font=sans, fill="#A8AFB8")

nodes = ["用户输入", "知识检索", "LLM", "输出"]
y = 236
for i, text in enumerate(nodes):
    draw.rounded_rectangle((34, y, W - 34, y + 54), radius=9, outline="#383E46", fill="#1C1F24", width=1)
    draw.ellipse((50, y + 22, 60, y + 32), fill="#82B7A6")
    draw.text((72, y + 16), text, font=label, fill="#E9E6DF")
    draw.text((W - 52, y + 19), f"0{i + 1}", font=mono, fill="#5D626B")
    if i < len(nodes) - 1:
        draw.line((W // 2, y + 54, W // 2, y + 76), fill="#33383F", width=1)
    y += 76

draw.line((34, 612, W - 34, 612), fill="#2A2F36", width=1)
draw.text((34, 634), "知识库 6 篇", font=sans, fill="#8B9199")
draw.text((34, 662), "用例 5 条 · Top1 0.78", font=sans, fill="#8B9199")

path = os.path.join(OUT, "agent-cover.webp")
cover.convert("RGB").save(path, "WEBP", quality=90, method=6)
print("agent-cover.webp", cover.size, round(os.path.getsize(path) / 1024, 1), "KB")
