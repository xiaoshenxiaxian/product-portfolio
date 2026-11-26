# -*- coding: utf-8 -*-
"""生成无照片版（最素版）：从当前带照片的 HTML 去掉头像并导出。"""
import io

D = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理"
src = D + r"\沈俊辉-产品助理-素版-2026.html"
dst = D + r"\沈俊辉-产品助理-素版-无照片-2026.html"

s = io.open(src, encoding="utf-8").read()

# 去掉头像
s = s.replace('        <img class="photo" src="photo.webp" alt="沈俊辉" />\n', "")
# 头部不再需要两端对齐（留着也无害，但保持居中更干净）
s = s.replace(
    "      .head { display: flex; align-items: flex-start; justify-content: space-between; gap: 8mm; }",
    "      .head { display: block; }",
)

io.open(dst, "w", encoding="utf-8").write(s)
print("photo removed:", '<img class="photo"' not in s)
