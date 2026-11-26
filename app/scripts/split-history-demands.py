# -*- coding: utf-8 -*-
"""把 history-demands.json 拆成 20 个 md，供上传到 Dify 知识库。"""
import io
import json
import os

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\agent-kit"
SRC = BASE + r"\tool-data\history-demands.json"
OUT = BASE + r"\tool-data\docs"

os.makedirs(OUT, exist_ok=True)
data = json.load(io.open(SRC, encoding="utf-8"))

for rec in data["记录"]:
    lines = [
        f"# {rec['id']} · {rec['module']}",
        "",
        f"> type: 历史需求 ｜ module: {rec['module']} ｜ 关键词：{rec['complaint'][:18]}",
        "",
        f"## 客户原话\n{rec['complaint']}",
        "",
        f"## 涉及角色\n{'、'.join(rec['roles'])}",
        "",
        f"## 状态\n{'、'.join(rec['states'])}",
        "",
        f"## 异常\n{'、'.join(rec['exceptions'])}",
        "",
        f"## 验收口径\n{rec['acceptance']}",
        "",
        f"## 当时的结论\n{rec['conclusion']}",
    ]
    path = os.path.join(OUT, f"{rec['id']}.md")
    io.open(path, "w", encoding="utf-8").write("\n".join(lines))

print("docs:", len(data["记录"]), "->", OUT)
