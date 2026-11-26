# -*- coding: utf-8 -*-
"""逐条抽取开头与置信度，判断类型化行为。"""
import csv
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\result.csv"
raw = io.open(path, encoding="utf-8-sig", newline="").read()
rows = list(csv.reader(io.StringIO(raw)))[1:]

for i, r in enumerate(rows, 1):
    out = r[3] if len(r) > 3 else ""
    head = re.sub(r"\s+", " ", out)[:150]
    conf = re.search(r"置信度[：:\s]*([a-zA-Z\u4e00-\u9fa5]{1,6})", out)
    refuse = "拒答" in out or "无法回答" in out or "超出范围" in out or "不在能力范围" in out
    ask = out.count("？") + out.count("?")
    print(f"[{i:02d}] conf={conf.group(1) if conf else '-':6s} 问号={ask:3d} 拒答={'Y' if refuse else 'N'} | {head}")
