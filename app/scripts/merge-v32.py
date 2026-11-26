# -*- coding: utf-8 -*-
"""合并三批结果 → 清洗 → 生成可读表 + 打印信号。"""
import csv
import io
import json
import re
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品"
SRCS = [f"{BASE}\\result1.csv", f"{BASE}\\result2.csv", f"{BASE}\\result3.csv"]
OUT = f"{BASE}\\result-可读.xlsx"

CASES = [f"A0{i}" for i in range(1, 9)] + [f"B0{i}" for i in range(1, 7)] + \
        [f"C0{i}" for i in range(1, 5)] + [f"D0{i}" for i in range(1, 5)] + \
        [f"E0{i}" for i in range(1, 5)] + [f"F0{i}" for i in range(1, 4)] + ["G01"]


def clean(raw: str) -> str:
    text = raw or ""
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            vals = [v for v in obj.values() if isinstance(v, str)]
            if vals:
                text = max(vals, key=len)
    except Exception:
        pass
    text = re.sub(r"<think>.*?(</think>|$)", "", text, flags=re.S)
    text = re.sub(r"</?think>", "", text)
    text = text.replace("\\n", "\n").replace("\\t", "\t").replace('\\"', '"')
    return text.strip().strip('"').strip()


rows = []
for p in SRCS:
    part = list(csv.reader(io.StringIO(io.open(p, encoding="utf-8-sig", newline="").read())))[1:]
    rows.extend(part)

print("合并行数:", len(rows))

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "v3.2 结果"
ws.append(["编号", "输入", "输出（已清理）", "字数"])

for i, r in enumerate(rows):
    cid = CASES[i] if i < len(CASES) else f"#{i+1}"
    inp = r[0] if r else ""
    out = clean(r[3] if len(r) > 3 else "")
    ws.append([cid, inp, out, len(out)])

    txt = str(out)
    conf = re.search(r"置信度[：:\s]*([a-zA-Z\u4e00-\u9fa5]{1,8})", txt)
    plan = ("主流程" in txt) and ("异常" in txt)
    wait_only = ("不出具方案" in txt) or (txt.count("待确认") > 5 and not plan)
    head = re.sub(r"\s+", " ", txt)[:70]
    flag = "方案" if plan else ("只问" if wait_only else "?")
    print(f"[{cid}] {len(txt):5}字 {flag:2s} conf={(conf.group(1) if conf else '-'):4s} | {head}")

for i, w in enumerate([8, 28, 95, 8], 1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.freeze_panes = "A2"
for c in range(1, 5):
    cell = ws.cell(row=1, column=c)
    cell.fill = PatternFill("solid", fgColor="12463C")
    cell.font = Font(color="FFFFFF", bold=True)
    cell.alignment = Alignment(horizontal="center")
for r in range(2, ws.max_row + 1):
    ws.row_dimensions[r].height = 110
    for c in range(1, 5):
        ws.cell(row=r, column=c).alignment = Alignment(vertical="top", wrap_text=True)
        ws.cell(row=r, column=c).font = Font(size=9)

wb.save(OUT)
print("saved", OUT)
