# -*- coding: utf-8 -*-
"""看两条完整输出：A01（完整场景）与 B01（模糊需求），去掉思维链部分。"""
import csv
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\result.csv"
rows = list(csv.reader(io.StringIO(io.open(path, encoding="utf-8-sig", newline="").read())))[1:]

for idx in (0, 8, 26):
    out = rows[idx][3]
    # 去掉 think 段
    body = re.sub(r"<think>.*?<｜end▁of▁thinking｜>", "", out, flags=re.S)
    if body == out:
        # 没有闭合，取 think 之后
        body = out.split("</think>")[-1]
    body = re.sub(r"\s+", " ", body).strip()
    print(f"\n===== 第 {idx+1} 条 =====\n{body[:900]}\n")
