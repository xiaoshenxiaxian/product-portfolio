# -*- coding: utf-8 -*-
"""压缩：实习两条并一条，Agent 去掉兜底条，压回一页。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI产品-ToC-白日梦-2026.html"
s = io.open(p, encoding="utf-8").read()
before = s

old_intern = '''          <li><b>问题：</b>从浏览到支付有 5 类中途失败（支付失败、超时、认证不过），客服答不上「到哪了」，运营说不清卡在哪一步。</li>
          <li><b>动作与结果：</b>把 6 个状态、5 类失败画成一张流转图，写成 <b>8 页 PRD</b>——每个字段谁能改、出错了怎么兜、怎么验收；送审后跟研发联调、按文档逐条核对；初稿先用 AI 出，再逐条核。</li>'''
new_intern = '''          <li><b>动作与结果：</b>从浏览到支付有 5 类中途失败，客服答不上「到哪了」——把 6 个状态、5 类失败画成流转图，写成 <b>8 页 PRD</b>（每个字段谁能改、出错怎么兜、怎么验收）；送审后跟研发联调逐条核对，初稿先用 AI 出。</li>'''
if old_intern in s:
    s = s.replace(old_intern, new_intern)
    print("intern merged")
else:
    print("MISS intern")

old_fd = '''          <li><b>兜底：</b>写 2 页运行手册（坏了怎么修、改版怎么回滚、成本与限流），边界写明「单场景、无权限与审计」。</li>
'''
if old_fd in s:
    s = s.replace(old_fd, "")
    print("fd removed")
else:
    print("MISS fd")

io.open(p, "w", encoding="utf-8").write(s)
print("changed:", s != before)
