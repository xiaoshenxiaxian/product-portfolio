# -*- coding: utf-8 -*-
"""把 30 条评测集拆成 3 批（每批 10 条），规避知识库检索限流。"""
import csv
import io

SRC = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\需求拆解Agent-评测集-30条.csv"
OUT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理"

rows = list(csv.reader(io.open(SRC, encoding="utf-8", newline="")))
header, data = rows[0], rows[1:]

for i in range(3):
    part = data[i * 10:(i + 1) * 10]
    path = f"{OUT}\\需求拆解Agent-评测集-第{i+1}批.csv"
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(part)
    print(path, len(part), "行")
