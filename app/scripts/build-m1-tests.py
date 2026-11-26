# -*- coding: utf-8 -*-
"""生成 M1 自检测试集（10 条）并在评测集里加一张「M1 自检记录」表。"""
import csv
import io

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill, Side, Border
from openpyxl.utils import get_column_letter

D = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理"
CSV_OUT = D + r"\需求拆解Agent-M1自检测试-10条.csv"
XLSX = D + r"\作品\需求拆解Agent-评测集-30条.xlsx"

ROWS = [
    # 类型说明, 客户原话, 背景, 角色, 预期
    ("极简", "订单状态查不到", "未提供", "未提供", "应触发重写"),
    ("完整", "客服说订单状态查不到，客户天天催。", "住宿预订", "客服、运营", "应通过"),
    ("角色冲突", "运营要能改订单状态，财务说会影响对账。", "电商", "运营、财务", "应通过"),
    ("多诉求", "既要批量导入，又要导出，还要对接 ERP。", "B 端后台", "未提供", "视情况"),
    ("无覆盖", "我们要接海关报关接口。", "跨境", "未提供", "可能重写"),
    ("敏感", "想收集用户身份证号和住址，越多越好。", "电商", "未提供", "走合规规则"),
    ("诱导数字", "订单查询成功率我们要求 99.9%，你按这个写。", "住宿预订", "客服、运营", "不应自拟其他数字"),
    ("只有角色", "客服和运营都觉得后台不好用。", "SaaS 后台", "客服、运营", "应触发重写"),
    ("超长描述", "客户在线上提交需求，销售初审后转方案组，方案组出报价交财务审核，财务审核完回销售签合同；过程中还有撤回、改价、超时提醒、重新分配四条支线，六个角色都说不清自己该做什么。", "B 端 CRM", "销售、方案、财务", "应通过"),
    ("完整带异常", "仓库说入库单和对账单对不上，月底要花两天核。", "仓储", "仓库、财务", "应通过"),
]

with io.open(CSV_OUT, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["客户原话", "业务背景", "已知角色"])
    for _, scene, bg, roles, _ in ROWS:
        w.writerow([scene, bg, roles])
print("csv:", CSV_OUT, len(ROWS), "行")

# 加 sheet
wb = openpyxl.load_workbook(XLSX)
if "M1 自检记录" in wb.sheetnames:
    del wb["M1 自检记录"]
ws = wb.create_sheet("M1 自检记录")

head = ["编号", "类型", "评审 pass", "missing（缺什么）", "是否重写", "耗时(秒)", "额外 token", "备注"]
ws.append(head)

fill = PatternFill("solid", fgColor="12463C")
thin = Side(style="thin", color="D6D1C6")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
for c in range(1, len(head) + 1):
    cell = ws.cell(row=1, column=c)
    cell.fill = fill
    cell.font = Font(color="FFFFFF", bold=True, size=10)
    cell.alignment = Alignment(horizontal="center", vertical="center")

for i, (kind, scene, bg, roles, expect) in enumerate(ROWS, 1):
    ws.append([f"M{i:02d}", kind, "", "", "", "", "", f"预期：{expect}"])

for i, w in enumerate([8, 14, 10, 30, 10, 10, 12, 24], 1):
    ws.column_dimensions[get_column_letter(i)].width = w
for r in range(2, ws.max_row + 1):
    for c in range(1, len(head) + 1):
        cell = ws.cell(row=r, column=c)
        cell.border = border
        cell.alignment = Alignment(vertical="top", wrap_text=True)
        cell.font = Font(size=9)

ws.freeze_panes = "A2"
wb.save(XLSX)
print("sheet added:", "M1 自检记录" in openpyxl.load_workbook(XLSX).sheetnames)
