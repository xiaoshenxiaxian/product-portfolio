# -*- coding: utf-8 -*-
"""白日梦版：爪伴提到第一位，摘要写「自己养猫 + 宠物产品」，删掉桌面美化腾空间。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI产品-ToC-白日梦-2026.html"
s = io.open(p, encoding="utf-8").read()
before = s

# 1) 摘要：养猫 + 爪伴 + 差评 + AI
old_sum_start = "做过三件和用户有关的事："
i = s.index(old_sum_start)
j = s.index("</p>", i)
new_sum = ("自己养猫，做过一个宠物领养产品（12 屏 C 端 + 审核后台）——把「领养不是下单」拆成健康验证、"
           "救助故事和 <b>4 步可追踪审核</b>；也把 <b>50 条差评</b>逐条分类定位主因，用 Dify 自己搭了个 AI 工具，"
           "建 <b>30 条评测集</b>从 19/30 到 29/30。习惯先看用户怎么做，再决定做什么。")
s = s[:i] + new_sum + s[j:]

# 2) 在「观境」前插入爪伴
anchor = '        <div class="entry">\n          <div class="row">\n            <span>观境文旅'
zhuaban = '''        <div class="entry">
          <div class="row">
            <span>爪伴 · 同城领养 ｜ <span class="role">宠物 ToC · 个人项目</span></span>
            <span>2025.12 – 2026.05</span>
          </div>
          <ul>
            <li><b>问题：</b>领养不是下单——领养人怕遇到骗子，送养人怕遇到虐宠，两边都不敢先信。</li>
            <li><b>动作与结果：</b>把「信任」拆成健康验证（疫苗 / 驱虫 / 绝育可查）、救助故事（来源 / 性格 / 习惯）和 <b>4 步可追踪审核</b>（提交 → 初审 → 沟通家访 → 完成），补驳回、补材料、改期等 <b>6 个分支</b>；交付 <b>12 屏 C 端 + 审核后台</b>，领养人 / 送养人 / 志愿者各看各的。</li>
          </ul>
        </div>
'''
if anchor in s:
    s = s.replace(anchor, zhuaban + anchor, 1)
else:
    print("MISS anchor 观境")

# 3) 删掉桌面美化整块（空间不够，差评分析已在摘要）
k = s.find('<span>桌面美化 App')
if k != -1:
    start = s.rfind('<div class="entry">', 0, k)
    end = s.find('</div>', s.find('</ul>', k)) + len('</div>')
    s = s[:start] + s[end:]
    print("desktop removed")
else:
    print("MISS desktop")

# 4) 观境两条并一条
old_gj = '''            <li><b>问题：</b>C 端购票和后台核销各写各的状态，改一处要改十页。</li>
            <li><b>动作与结果：</b>把订单拆成 6 个状态、4 类异常，两边用同一套说法；请 <b>12 位试用者</b>走原型，发现「主链路和支线太多」，据此砍掉支线，主链路从 <b>5 步减到 3 步</b>。</li>'''
new_gj = '''            <li><b>动作与结果：</b>把订单拆成 6 个状态、4 类异常，让前台后台用同一套说法；请 <b>12 位试用者</b>走原型，反馈「主链路和支线太多」，据此砍掉支线，主链路从 <b>5 步减到 3 步</b>。</li>'''
if old_gj in s:
    s = s.replace(old_gj, new_gj)
else:
    print("MISS guanjing")

# 5) 实习两条并一条
old_intern = '''            <li><b>问题：</b>从浏览到支付有 5 类中途失败（支付失败、超时、认证不过），客服答不上「到哪了」，运营说不清卡在哪一步。</li>
            <li><b>动作与结果：</b>把 6 个状态、5 类失败画成一张流转图，写成 <b>8 页 PRD</b>——每个字段谁能改、出错了怎么兜、怎么验收；送审后跟研发联调、按文档逐条核对；初稿先用 AI 出，再逐条核。</li>'''
new_intern = '''            <li><b>动作与结果：</b>从浏览到支付有 5 类中途失败，客服答不上「到哪了」——把 6 个状态、5 类失败画成流转图，写成 <b>8 页 PRD</b>（每个字段谁能改、出错怎么兜、怎么验收）；送审后跟研发联调逐条核对，初稿先用 AI 出。</li>'''
if old_intern in s:
    s = s.replace(old_intern, new_intern)
else:
    print("MISS intern")

io.open(p, "w", encoding="utf-8").write(s)
print("changed:", s != before)
