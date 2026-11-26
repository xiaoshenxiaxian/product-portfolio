# -*- coding: utf-8 -*-
"""把 Dify 批量运行结果（JSON 外壳 + \n 转义 + <think>）还原成可读表格。

用法：
    python clean-result.py <result.csv> <输出.xlsx>
"""
import csv
import io
import json
import re
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

src = sys.argv[1] if len(sys.argv) > 1 else r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\result.csv"
dst = sys.argv[2] if len(sys.argv) > 2 else src.replace(".csv", "-可读.xlsx")

CASES = ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08",
         "B01", "B02", "B03", "B04", "B05", "B06",
         "C01", "C02", "C03", "C04",
         "D01", "D02", "D03", "D04",
         "E01", "E02", "E03", "E04",
         "F01", "F02", "F03", "G01"]


def clean(raw: str) -> str:
    text = raw or ""
    # 1) 解 JSON 外壳
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            vals = [v for v in obj.values() if isinstance(v, str)]
            if vals:
                text = max(vals, key=len)
    except Exception:
        pass
    # 2) 去推理标签
    text = re.sub(r"<think>.*?(</think>|$)", "", text, flags=re.S)
    text = re.sub(r"</?think>", "", text)
    # 3) 还原转义
    text = text.replace("\\n", "\n").replace("\\t", "\t").replace('\\"', '"')
    # 4) 收尾
    text = text.strip().strip('"').strip()
    return text


rows = list(csv.reader(io.StringIO(io.open(src, encoding="utf-8-sig", newline="").read())))
header, data = rows[0], rows[1:]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "运行结果"
ws.append(["编号", "输入", "输出（已清理）", "字数"])

for i, r in enumerate(data):
    cid = CASES[i] if i < len(CASES) else f"#{i+1}"
    inp = r[0] if len(r) > 0 else ""
    out = clean(r[3] if len(r) > 3 else "")
    ws.append([cid, inp, out, len(out)])

widths = [8, 30, 100, 8]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws.freeze_panes = "A2"
head_fill = PatternFill("solid", fgColor="12463C")
for c in range(1, 5):
    cell = ws.cell(row=1, column=c)
    cell.fill = head_fill
    cell.font = Font(color="FFFFFF", bold=True)
    cell.alignment = Alignment(horizontal="center")

for r in range(2, ws.max_row + 1):
    ws.row_dimensions[r].height = 120
    for c in range(1, 5):
        cell = ws.cell(row=r, column=c)
        cell.alignment = Alignment(vertical="top", wrap_text=True)
        cell.font = Font(size=9)

wb.save(dst)
print("saved", dst, "| rows:", len(data))
