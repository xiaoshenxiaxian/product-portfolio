# -*- coding: utf-8 -*-
"""领星版补教育背景，字号调 9.8pt。"""
import io

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品经理-领星-2026.html"
s = io.open(path, encoding="utf-8").read()

edu = """      <h2>教育背景</h2>
      <div class="entry">
        <div class="row"><span>阳光学院 ｜ 计算机科学与技术 · 本科（专升本）</span><span>2024.09 – 2026.06 ｜ CET-4</span></div>
      </div>

"""
if "教育背景" not in s:
    s = s.replace("      <h2>实习经历</h2>", edu + "      <h2>实习经历</h2>")

s = s.replace("font-size: 9.5pt; line-height: 1.55;", "font-size: 9.8pt; line-height: 1.6;")

io.open(path, "w", encoding="utf-8").write(s)
print("edu:", "教育背景" in s, "| 9.8pt:", "9.8pt" in s)
