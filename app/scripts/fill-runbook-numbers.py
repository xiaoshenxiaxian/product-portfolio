# -*- coding: utf-8 -*-
"""运行手册填入模型名、限流来源与今日消耗。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-需求拆解Agent-运行手册.html"
s = io.open(p, encoding="utf-8").read()

s = s.replace(
    "平台：Dify 工作流 ｜ 模型：<span class=\"fill\">［填模型名］</span> ｜ 知识库：6 篇 ｜ 版本：v3.2 ｜ 更新：2026-11",
    "平台：Dify 工作流 ｜ 模型：DeepSeek V4.1 Flash（deepseek-flash） ｜ 知识库：6 篇 ｜ 版本：v3.2 ｜ 更新：2026-11",
)

s = s.replace(
    '<tr><td>限流</td><td>批量 30 条会触发知识库检索限流，建议每批 10 条、间隔 3 分钟</td><td><span class="fill">［填实际配额］</span></td></tr>',
    '<tr><td>限流</td><td>批量 30 条会撞 <b>Dify 知识库检索配额</b>（报错：knowledge base request rate limit），不是模型限流</td><td>改每批 10 条、间隔 3 分钟</td></tr>',
)

s = s.replace(
    '<tr><td>未做的部分</td><td>没有权限与审计、没有接工单系统、知识库无维护机制、无监控告警</td></tr>',
    '<tr><td>未做的部分</td><td>无权限与审计、未接工单系统、知识库无维护机制、无监控告警</td></tr>\n'
    '          <tr><td>调用成本</td><td>单次约 3–4 万 tokens（含检索上下文）；<b>缓存命中占 99.6%</b>，实际计费很低</td></tr>\n'
    '          <tr><td>实测消耗</td><td>2026-11-25 当日 1.128 亿 tokens（命中 1.124 亿 / 未命中 21 万 / 输出 22 万）</td></tr>',
)

io.open(p, "w", encoding="utf-8").write(s)
print("model:", "deepseek-flash" in s, "| cost:", "1.128 亿" in s)
