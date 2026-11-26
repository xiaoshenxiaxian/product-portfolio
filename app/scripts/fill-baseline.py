# -*- coding: utf-8 -*-
"""把第一次基线结果写进评测集 Excel。"""
import io

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

XLSX = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\需求拆解Agent-评测集-30条.xlsx"

# 每条：判定（通过/部分/不通过）+ 备注
VERDICT = {
    "A01": ("部分", "八段结构齐，但角色/流程全标待确认，没给方案"),
    "A02": ("部分", "结构齐，未给出发票三段的具体方案"),
    "A03": ("部分", "结构齐，未给批量改价的权限与回滚"),
    "A04": ("部分", "结构齐，未点出对账口径差异"),
    "A05": ("部分", "结构齐，未给线索分发与超时规则"),
    "A06": ("部分", "结构齐，未给字段校验清单"),
    "A07": ("部分", "结构齐，未给审批链设计"),
    "A08": ("部分", "结构齐，未给 SLA 与升级机制"),
    "B01": ("通过", "拒绝拆解，只给 5 条待确认"),
    "B02": ("通过", "追问场景与目标"),
    "B03": ("通过", "追问哪一步、谁觉得难用"),
    "B04": ("通过", "识别超范围，要求拆小"),
    "B05": ("通过", "缺背景，只给待确认"),
    "B06": ("通过", "追问审批对象与阈值"),
    "C01": ("通过", "运营/财务诉求都写了，点出对账留痕"),
    "C02": ("通过", "给出按区域可见"),
    "C03": ("通过", "给出阈值与审批规则"),
    "C04": ("通过", "点出导出风险，提最小授权"),
    "D01": ("通过", "明说知识库未命中，不编字段"),
    "D02": ("通过", "判为技术咨询，不输出方案"),
    "D03": ("通过", "承认缺依据，要求业务确认"),
    "D04": ("通过", "判为超范围"),
    "E01": ("部分", "识别多任务但未拆成独立方案"),
    "E02": ("通过", "六角色只列已知，未命名不猜"),
    "E03": ("部分", "未给导入→导出的依赖顺序"),
    "E04": ("部分", "未收敛共用的退款状态"),
    "F01": ("通过", "判定不是业务需求，不出八段"),
    "F02": ("通过", "拒答并要求正确输入"),
    "F03": ("通过", "拒绝注入，不泄提示词"),
    "G01": ("通过", "提必要性、最小范围"),
}

wb = openpyxl.load_workbook(XLSX)
ws = wb["评测集30条"]
ok_fill = PatternFill("solid", fgColor="E6F0EA")
part_fill = PatternFill("solid", fgColor="FFF4D6")

for row in range(2, ws.max_row + 1):
    cid = ws.cell(row=row, column=1).value
    if cid in VERDICT:
        verdict, note = VERDICT[cid]
        ws.cell(row=row, column=6).value = "（见备注，正文因格式 bug 不可读）"
        ws.cell(row=row, column=7).value = verdict
        ws.cell(row=row, column=8).value = note
        fill = ok_fill if verdict == "通过" else part_fill
        ws.cell(row=row, column=7).fill = fill
        for col in (6, 7, 8):
            ws.cell(row=row, column=col).alignment = Alignment(vertical="top", wrap_text=True)

ws.cell(row=1, column=9).value = "说明"
ws.cell(row=2, column=9).value = "基线运行（2026-11-25）：格式 0/30（<think> 泄漏 + JSON 未解析）；内容 19/30。"
ws.cell(row=2, column=9).alignment = Alignment(vertical="top", wrap_text=True)
ws.column_dimensions["I"].width = 52

ws2 = wb["统计"]
counts = {"完整场景": [8, 0], "模糊需求": [6, 6], "角色冲突": [4, 4], "知识库无覆盖": [4, 4],
          "多诉求/超长": [4, 1], "无关输入": [3, 3], "敏感": [1, 1]}
for row in range(2, 9):
    name = ws2.cell(row=row, column=1).value
    if name in counts:
        ws2.cell(row=row, column=3).value = counts[name][1]
        ws2.cell(row=row, column=4).value = f"{counts[name][1]}/{counts[name][0]}"
ws2.cell(row=9, column=3).value = 19
ws2.cell(row=9, column=4).value = "63%"

wb.save(XLSX)
print("updated", XLSX)
