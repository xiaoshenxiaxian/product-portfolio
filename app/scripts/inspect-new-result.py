# -*- coding: utf-8 -*-
"""查看新的运行结果：格式是否干净、A 类是否给方案。"""
import re
import sys

import openpyxl

sys.stdout.reconfigure(encoding="utf-8")

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\result-可读.xlsx"
wb = openpyxl.load_workbook(path)
ws = wb.active
print("rows:", ws.max_row - 1, "| header:", [c.value for c in ws[1]])

for row in ws.iter_rows(min_row=2, values_only=True):
    cid, inp, out, n = row[0], row[1], row[2] or "", row[3]
    txt = str(out)
    conf = re.search(r"置信度[：:\s]*([a-zA-Z\u4e00-\u9fa5]{1,8})", txt)
    think = "<think>" in txt
    marks = txt.count("？") + txt.count("?")
    plan = ("主流程" in txt) or ("异常分支" in txt)
    wait_only = txt.count("待确认") > 6 and not plan
    head = re.sub(r"\s+", " ", txt)[:90]
    print(f"[{cid}] {n:5} 字 think={'Y' if think else 'N'} 问号={marks:2d} 含流程/异常={'Y' if plan else 'N'} 纯待确认={'Y' if wait_only else 'N'} conf={(conf.group(1) if conf else '-'):4s} | {head}")
