# -*- coding: utf-8 -*-
"""把 Dify 截图按原生分辨率转成 WebP（不再缩小），供灯箱按原尺寸显示。"""
import glob
import os

from PIL import Image

OUT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\public\work"
ATT = r"C:\Users\18759\.dsh\attachments\v1\objects"


def find(sha):
    matches = glob.glob(os.path.join(ATT, sha[:2], sha + "*"))
    if not matches:
        raise SystemExit("missing attachment: " + sha)
    return matches[0]


def save(img, name, quality=90):
    path = os.path.join(OUT, name)
    img.convert("RGB").save(path, "WEBP", quality=quality, method=6)
    print(name, img.size, round(os.path.getsize(path) / 1024, 1), "KB")


canvas = Image.open(find("8f30b5c011100bb36f81a6686329a410ec63448cf588e08e8d693385f9df1a8c"))
save(canvas, "agent-canvas.webp", 92)

recall = Image.open(find("82408fc0976985e36e92617654f77a88e009b572005dad15994184b85c41f256"))
save(recall, "agent-recall.webp", 92)

run = Image.open(find("6bd0417e3e62758b2b85f6d28ce85c5e6bb32f5a766af425264d3f5381dd076f"))
save(run, "agent-run.webp", 88)

app = Image.open(find("6f1ad488da571c7a19b7461b549e6718fe2449bbda90a486f1f487b872642909"))
save(app, "agent-app.webp", 92)
