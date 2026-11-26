# -*- coding: utf-8 -*-
"""在评测集里加「轨迹评测」表（M4 用）。"""
import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

XLSX = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\需求拆解Agent-评测集-30条.xlsx"

wb = openpyxl.load_workbook(XLSX)
if "轨迹评测" in wb.sheetnames:
    del wb["轨迹评测"]

ws = wb.create_sheet("轨迹评测")
head = ["编号", "成功", "步数", "调了哪些工具", "是否重写", "耗时(秒)", "token", "成本(元)", "失败原因"]
ws.append(head)

fill = PatternFill("solid", fgColor="12463C")
thin = Side(style="thin", color="D6D1C6")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
for c in range(1, len(head) + 1):
    cell = ws.cell(row=1, column=c)
    cell.fill = fill
    cell.font = Font(color="FFFFFF", bold=True, size=10)
    cell.alignment = Alignment(horizontal="center", vertical="center")

CASES = [f"A{i:02d}" for i in range(1, 9)] + [f"B{i:02d}" for i in range(1, 7)] + \
        [f"C{i:02d}" for i in range(1, 5)] + [f"D{i:02d}" for i in range(1, 5)] + \
        [f"E{i:02d}" for i in range(1, 5)] + [f"F{i:02d}" for i in range(1, 4)] + ["G01"]

for cid in CASES:
    ws.append([cid, "", "", "", "", "", "", "", ""])

for i, w in enumerate([8, 8, 8, 24, 10, 10, 10, 10, 28], 1):
    ws.column_dimensions[get_column_letter(i)].width = w
for r in range(2, ws.max_row + 1):
    for c in range(1, len(head) + 1):
        cell = ws.cell(row=r, column=c)
        cell.border = border
        cell.font = Font(size=9)
        cell.alignment = Alignment(vertical="top", wrap_text=True)

ws.freeze_panes = "A2"
ws.cell(row=len(CASES) + 3, column=1).value = "失败原因取值：没调工具 / 调错工具 / 不收敛（触顶）/ 输出不合格 / 工具报错"
ws.cell(row=len(CASES) + 3, column=1).font = Font(size=9, italic=True)

wb.save(XLSX)
print("轨迹评测 added:", "轨迹评测" in openpyxl.load_workbook(XLSX).sheetnames)
