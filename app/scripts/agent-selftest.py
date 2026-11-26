# -*- coding: utf-8 -*-
"""四版简历统一 Agent 表述为：原型 · 单场景 · 个人自测。"""
import io
import re

base = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理"
files = [
    "沈俊辉-AI管培生-蓝凌-2026.html",
    "沈俊辉-产品经理-领星-2026.html",
    "沈俊辉-产品专员-阿里云Agent-2026.html",
    "沈俊辉-产品助理-达酷互动-2026.html",
]

for name in files:
    path = base + "\\" + name
    s = io.open(path, encoding="utf-8").read()
    before = s

    # 已改为「原型」的版本：换掉试用说法
    s = s.replace("单场景 · 内部试用", "单场景 · 个人自测")
    # 尚未改的版本：整条替换
    s = re.sub(
        r"需求拆解 Agent ｜ <span class=\"role\">Dify 工作流 \+ 知识库 · 个人项目</span>",
        '需求拆解 Agent 原型 ｜ <span class="role">Dify 工作流 + 知识库 · 单场景 · 个人自测</span>',
        s,
    )
    s = re.sub(
        r"需求拆解 Agent ｜ <span class=\"role\">Dify 工作流 \+ 知识库 · 个人项目 · 未上线</span>",
        '需求拆解 Agent 原型 ｜ <span class="role">Dify 工作流 + 知识库 · 单场景 · 个人自测</span>',
        s,
    )

    io.open(path, "w", encoding="utf-8").write(s)
    print(name, "| changed:", s != before, "| 自测:", "个人自测" in s)
