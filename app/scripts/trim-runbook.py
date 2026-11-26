# -*- coding: utf-8 -*-
"""运行手册压到一页：把第 7 节并进第 6 节。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-需求拆解Agent-运行手册.html"
s = io.open(p, encoding="utf-8").read()

start = s.index('      <h2>7 交接给下一个人时要一起给的东西</h2>')
end = s.index('      <p class="foot">')
s = s[:start] + s[end:]

s = s.replace(
    '<tr><td>模型成本</td><td><span class="fill">［填单次约多少 token / 多少钱］</span></td></tr>',
    '<tr><td>模型成本</td><td><span class="fill">［填单次约多少 token / 多少钱］</span></td></tr>\n'
    '          <tr><td>交接时一起给</td><td>本手册 · 评测集 30 条与最近一次结果 · 提示词（含版本记录）· 知识库 6 篇（维护人 / 更新日 / 适用范围）· 一个已知失败的例子</td></tr>',
)

io.open(p, "w", encoding="utf-8").write(s)
print("ok:", "7 交接" not in s)
