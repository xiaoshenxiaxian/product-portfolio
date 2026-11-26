# -*- coding: utf-8 -*-
"""两版简历把 Agent 表述为「原型 · 单场景 · 内部试用」。"""
import io

files = [
    r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI管培生-蓝凌-2026.html",
    r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品经理-领星-2026.html",
]

pairs = [
    (
        '<span>需求拆解 Agent ｜ <span class="role">Dify 工作流 + 知识库 · 个人项目 · 未上线</span></span>',
        '<span>需求拆解 Agent 原型 ｜ <span class="role">Dify 工作流 + 知识库 · 单场景 · 内部试用</span></span>',
    ),
    (
        '<span>需求拆解 Agent ｜ <span class="role">Dify 工作流 + 知识库 · 个人项目</span></span>',
        '<span>需求拆解 Agent 原型 ｜ <span class="role">Dify 工作流 + 知识库 · 单场景 · 内部试用</span></span>',
    ),
]

for path in files:
    s = io.open(path, encoding="utf-8").read()
    for a, b in pairs:
        s = s.replace(a, b)
    io.open(path, "w", encoding="utf-8").write(s)
    print(path.split("\\")[-1], "| ok:", "Agent 原型" in s)
