# -*- coding: utf-8 -*-
"""修正评测页附件：去掉不存在的 eval-baseline.pdf。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

s = s.replace(
    "      { label: '评测集（30 条 + 判定）', href: '/docs/eval-set.pdf' },\n"
    "      { label: '基线结果（19/30）', href: '/docs/eval-baseline.pdf' },\n"
    "      { label: '最终结果（29/30）', href: '/docs/eval-final.pdf' },",
    "      { label: '评测集（30 条 + 判定 + 版本对比）', href: '/docs/eval-set.pdf' },\n"
    "      { label: '最终结果（29/30 原始输出）', href: '/docs/eval-final.pdf' },",
)

io.open(p, "w", encoding="utf-8").write(s)
print("eval-baseline removed:", "eval-baseline" not in s)
