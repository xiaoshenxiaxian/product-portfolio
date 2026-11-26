# -*- coding: utf-8 -*-
"""从 30 条结果里挑 6 条，生成 demo 页数据。"""
import io
import json
import re

import openpyxl

SRC = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\作品\result-可读.xlsx"
OUT = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\agentDemo.js"

# 展示用：6 条，覆盖「出方案 / 追问 / 角色冲突 / 知识库无依据 / 多诉求 / 拒答」
PICK = [
    ("A01", "完整需求", "客户说：我们的订单状态查不到，客服天天被骂。", "住宿预订", "客服、运营"),
    ("C01", "角色冲突", "运营要能改订单状态，财务说不行，会影响对账。", "电商", "运营、财务"),
    ("B01", "模糊需求", "我想让系统更智能一点。", "未提供", "未提供"),
    ("D01", "知识库无依据", "我们要接海关报关接口。", "跨境", "未提供"),
    ("E02", "多诉求", "我们的业务流程是这样的：客户提交需求，销售初审后转方案组，方案组出报价交财务审核，财务审核完回到销售签合同。过程中有六个角色、四条支线，现在每个人都说不知道自己该做什么。", "B 端 CRM", "销售、方案、财务"),
    ("F01", "无关输入", "今天天气怎么样？", "未提供", "未提供"),
]

wb = openpyxl.load_workbook(SRC)
ws = wb.active
rows = {r[0]: r[2] for r in ws.iter_rows(min_row=2, values_only=True)}

items = []
for cid, label, scene, bg, roles in PICK:
    text = str(rows.get(cid) or "").strip()
    text = text.replace('\\\\n', '\n')
    items.append({"id": cid, "label": label, "scene": scene, "background": bg, "roles": roles, "output": text})

js = "// 真实运行结果（2026-11-25，v3.2），由 result-可读.xlsx 提取\nexport const demoCases = " + \
     json.dumps(items, ensure_ascii=False, indent=2) + "\n"

io.open(OUT, "w", encoding="utf-8").write(js)
print("saved", OUT, "| cases:", len(items), "| lengths:", [len(i["output"]) for i in items])
