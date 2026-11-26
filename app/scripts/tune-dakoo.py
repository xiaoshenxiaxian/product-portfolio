# -*- coding: utf-8 -*-
"""达酷互动版：字号调 10pt，补商业实践。"""
import io

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品助理-达酷互动-2026.html"
s = io.open(path, encoding="utf-8").read()

s = s.replace("font-size: 9.5pt; line-height: 1.55;", "font-size: 10pt; line-height: 1.62;")

business = """      <h2>商业运营实践</h2>
      <div class="entry">
        <div class="row">
          <span>家乡特产小店 ｜ 参与经营（选品、定价、备货、算账）</span>
          <span>2022 – 2026（节假日累计 <b>15 个月</b>）</span>
        </div>
        <ul>
          <li><b>把模糊需求问成具体的：</b>客人说「随便看看」，先问送人还是自用，再挑两三样讲清楚——哪种耐放、哪种拿得出手，不硬推。</li>
          <li><b>推荐完看结果：</b>20 元和 25 元两档最好卖，买单的主要是 28–55 岁；问过价的客人里约 <b>65%</b> 会买，哪类人配哪类货就照这个备货。</li>
        </ul>
      </div>

"""
s = s.replace('      <h2>技能</h2>', business + '      <h2>技能</h2>')

io.open(path, "w", encoding="utf-8").write(s)
print("ok")
