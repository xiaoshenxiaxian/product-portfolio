# -*- coding: utf-8 -*-
"""把 Dify 的截图转成作品集用图，并生成弧线封面。"""
import glob
import os

from PIL import Image, ImageDraw, ImageFont

OUT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\public\work"
ATT = r"C:\Users\18759\.dsh\attachments\v1\objects"


def find(sha):
    matches = glob.glob(os.path.join(ATT, sha[:2], sha + "*"))
    if not matches:
        raise SystemExit("missing attachment: " + sha)
    return matches[0]


def save_webp(img, name, quality=82):
    path = os.path.join(OUT, name)
    img.convert("RGB").save(path, "WEBP", quality=quality, method=6)
    print(name, img.size, round(os.path.getsize(path) / 1024, 1), "KB")


def fit_width(img, width):
    if img.width <= width:
        return img
    height = round(img.height * width / img.width)
    return img.resize((width, height), Image.LANCZOS)


# 1. 工作流画布
canvas = Image.open(find("8f30b5c011100bb36f81a6686329a410ec63448cf588e08e8d693385f9df1a8c"))
save_webp(fit_width(canvas, 1800), "agent-canvas.webp")

# 2. 召回测试
recall = Image.open(find("82408fc0976985e36e92617654f77a88e009b572005dad15994184b85c41f256"))
save_webp(fit_width(recall, 820), "agent-recall.webp")

# 3. 运行输出（截前 2300px）
run = Image.open(find("6bd0417e3e62758b2b85f6d28ce85c5e6bb32f5a766af425264d3f5381dd076f"))
run = run.crop((0, 0, run.width, min(run.height, 2300)))
save_webp(fit_width(run, 820), "agent-run.webp")

# 4. Web App 表单（裁掉右侧空白）
app = Image.open(find("6f1ad488da571c7a19b7461b549e6718fe2449bbda90a486f1f487b872642909"))
app = app.crop((0, 0, int(app.width * 0.58), app.height))
save_webp(fit_width(app, 1080), "agent-app.webp")

# 5. 弧线封面 360x779
W, H = 360, 779
cover = Image.new("RGB", (W, H), "#14161A")
draw = ImageDraw.Draw(cover)

serif = ImageFont.truetype(r"C:\Windows\Fonts\NotoSerifSC-VF.ttf", 46)
sans = ImageFont.truetype(r"C:\Windows\Fonts\NotoSansSC-VF.ttf", 13)
small = ImageFont.truetype(r"C:\Windows\Fonts\NotoSansSC-VF.ttf", 11)
mono = ImageFont.truetype(r"C:\Windows\Fonts\Bahnschrift.ttf", 11)

draw.text((34, 40), "AGENT / 2026", font=mono, fill="#7C838D")
draw.text((34, 86), "需求拆解", font=serif, fill="#E9E6DF")
draw.text((34, 148), "客户一句话 → 流程 · 角色 · 字段 · 验收", font=sans, fill="#9AA1AA")

nodes = ["用户输入", "知识检索", "LLM", "输出"]
y = 236
for i, label in enumerate(nodes):
    draw.rounded_rectangle((34, y, W - 34, y + 46), radius=8, outline="#33383F", fill="#1C1F24", width=1)
    draw.ellipse((48, y + 18, 58, y + 28), fill="#82B7A6")
    draw.text((70, y + 15), label, font=sans, fill="#E9E6DF")
    draw.text((W - 58, y + 16), f"0{i + 1}", font=mono, fill="#5D626B")
    if i < len(nodes) - 1:
        draw.line((W // 2, y + 46, W // 2, y + 66), fill="#33383F", width=1)
    y += 66

draw.line((34, 610, W - 34, 610), fill="#2A2F36", width=1)
draw.text((34, 630), "知识库 6 篇 · 用例 5 条", font=small, fill="#8B9199")
draw.text((34, 652), "召回 Top1 0.78", font=small, fill="#8B9199")
draw.text((34, 700), "Dify Workflow", font=mono, fill="#5D626B")

save_webp(cover, "agent-cover.webp", quality=90)
print("done")
