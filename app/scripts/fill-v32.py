# -*- coding: utf-8 -*-
"""把 v3.2 结果写入评测集，并生成三版对比页。"""
import io

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

XLSX = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\需求拆解Agent-评测集-30条.xlsx"

# v3.2 判定：29/30，仅 E03 未通过
FAIL = {"E03"}
wb = openpyxl.load_workbook(XLSX)
ws = wb["评测集30条"]

for row in range(2, ws.max_row + 1):
    cid = ws.cell(row=row, column=1).value
    if not cid:
        continue
    ok = cid not in FAIL
    ws.cell(row=row, column=7).value = "通过" if ok else "不通过"
    ws.cell(row=row, column=7).fill = PatternFill(
        "solid", fgColor="E6F0EA" if ok else "FBE3E3"
    )
    if not ok:
        ws.cell(row=row, column=8).value = (
            "多诉求被判 1 分（原因：没认定业务对象是「B 端后台」），仍只给待确认清单"
        )

ws.cell(row=1, column=10).value = "v3.2（2026-11-25）"
ws.cell(row=2, column=10).value = "29/30 · 97%：A 类 8/8、B 6/6、C 4/4、D 4/4、E 3/4、F 3/3、G 1/1；仅 E03 未过"
ws.cell(row=2, column=10).alignment = Alignment(vertical="top", wrap_text=True)
ws.column_dimensions["J"].width = 46

# 对比页
if "版本对比" in wb.sheetnames:
    del wb["版本对比"]
cmp = wb.create_sheet("版本对比")
rows = [
    ["类型", "条数", "v1 基线", "v3.1", "v3.2"],
    ["A 完整场景", 8, 0, 8, 8],
    ["B 模糊需求", 6, 6, 6, 6],
    ["C 角色冲突", 4, 4, 2, 4],
    ["D 知识库无覆盖", 4, 4, 4, 4],
    ["E 多诉求/超长", 4, 1, 1, 3],
    ["F 无关输入", 3, 3, 3, 3],
    ["G 敏感", 1, 1, 0, 1],
    ["合计", 30, 19, 24, 29],
    ["通过率", "", "63%", "80%", "97%"],
]
for r in rows:
    cmp.append(r)
cmp.column_dimensions["A"].width = 18
for col in "BCDE":
    cmp.column_dimensions[col].width = 11
for row in cmp.iter_rows(min_row=1, max_row=len(rows), max_col=5):
    for cell in row:
        cell.border = __import__("openpyxl").styles.Border(
            *([__import__("openpyxl").styles.Side(style="thin", color="D6D1C6")] * 4)
        )
        cell.alignment = Alignment(horizontal="center")
for c in range(1, 6):
    cmp.cell(row=1, column=c).fill = PatternFill("solid", fgColor="12463C")
    cmp.cell(row=1, column=c).font = Font(color="FFFFFF", bold=True)
for c in range(1, 6):
    cmp.cell(row=9, column=c).font = Font(bold=True)
    cmp.cell(row=10, column=c).font = Font(bold=True)

wb.save(XLSX)
print("updated", XLSX)
