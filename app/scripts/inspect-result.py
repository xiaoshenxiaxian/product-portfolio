# -*- coding: utf-8 -*-
"""读取 Dify 批量运行结果，打印结构 + 每条的关键信号。"""
import csv
import io
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\result.csv"
raw = io.open(path, encoding="utf-8-sig", newline="").read()
reader = csv.reader(io.StringIO(raw))
rows = list(reader)
print("rows:", len(rows))
print("header:", rows[0])

KEYS = ["待确认", "置信度", "角色", "流程", "字段", "异常", "验收", "请问", "无法", "没有依据", "不确定", "建议"]
for i, r in enumerate(rows[1:], 1):
    text = " ".join(r)
    hit = [k for k in KEYS if k in text]
    first_col = r[0][:34].replace("\n", " ")
    print(f"[{i:02d}] len={len(text):5d} keys={','.join(hit)[:44]:44s} | {first_col}")
