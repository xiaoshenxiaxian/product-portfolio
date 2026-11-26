# -*- coding: utf-8 -*-
"""把爪伴 PRD 改名并做两处修正，另存为新 docx。"""
import sys

from docx import Document

sys.stdout.reconfigure(encoding="utf-8")

src = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\同城宠物领养管理系统_产品需求文档PRD_沈俊辉.docx"
dst = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\爪伴-同城宠物领养管理系统-PRD-2026.docx"

doc = Document(src)

# 1) 标题加品牌名
title = doc.paragraphs[0]
if "爪伴" not in title.text:
    title.text = "爪伴 · 同城宠物领养管理系统"

# 2) 标题下补一行说明
para1 = doc.paragraphs[1]
note = para1.insert_paragraph_before(
    "产品名：爪伴 ｜ 系统：同城宠物领养管理系统 ｜ 个人毕业设计项目（2025.12 – 2026.05）"
)
note.style = para1.style

# 3) 领养状态机第一行：待审核 → 待审核 的自循环，改成「未提交 → 待审核」
table = doc.tables[4]
first_cell = table.rows[1].cells[0]
if first_cell.text.strip() == "待审核":
    first_cell.text = "未提交"

doc.save(dst)
print("saved", dst)
print("title:", doc.paragraphs[0].text)
print("note:", doc.paragraphs[1].text)
print("state row1:", table.rows[1].cells[0].text, "->", table.rows[1].cells[2].text)
