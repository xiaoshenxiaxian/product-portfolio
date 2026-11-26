# -*- coding: utf-8 -*-
"""插入爪伴条目（置顶），并把观境两条并一条。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI产品-ToC-白日梦-2026.html"
s = io.open(p, encoding="utf-8").read()
before = s

anchor = '''      <div class="entry">
        <div class="row">
          <span>观境文旅 ｜ <span class="role">0→1 做票务系统（C 端 + 后台）</span></span>'''

zhuaban = '''      <div class="entry">
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
    print("zhuaban inserted")
else:
    print("MISS anchor")

old_gj = '''          <li><b>问题：</b>C 端购票和后台核销各写各的状态，改一处要改十页。</li>
          <li><b>动作与结果：</b>把订单拆成 6 个状态、4 类异常，让前台和后台用同一套说法；请 <b>12 位试用者</b>走原型，砍掉支线，主链路从 <b>5 步减到 3 步</b>。</li>'''
new_gj = '''          <li><b>动作与结果：</b>前台后台原来各写各的状态、改一处要改十页——把订单拆成 6 个状态、4 类异常，两边用同一套说法；请 <b>12 位试用者</b>走原型，反馈「支线太多」，砍掉后主链路从 <b>5 步减到 3 步</b>。</li>'''
if old_gj in s:
    s = s.replace(old_gj, new_gj)
    print("guanjing merged")
else:
    print("MISS guanjing")

io.open(p, "w", encoding="utf-8").write(s)
print("changed:", s != before)
