# -*- coding: utf-8 -*-
"""商业实践压成两行、去掉「联合主理人」，字号调回 9.5pt。"""
import io
import re

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI管培生-蓝凌-2026.html"
s = io.open(path, encoding="utf-8").read()

# 1) 标题
s = s.replace(
    "家乡特产与手工艺品小店 ｜ 联合主理人 / 运营",
    "家乡特产小店 ｜ 参与经营（选品、定价、备货、算账）",
)

# 2) 两条 bullet 整体替换
old_block = re.search(
    r"<span>家乡特产小店.*?</ul>", s, re.S
)
new_block = """<span>家乡特产小店 ｜ 参与经营（选品、定价、备货、算账）</span>
          <span>2022 – 2026（节假日累计 <b>15 个月</b>）</span>
        </div>
        <ul>
          <li><b>账是自己算的：</b>进货、定价、压货都自己盯——卖不动的要降价清，压久了就是亏，第一次知道「库存」不是报表上的数字。</li>
          <li><b>客人不是一类人：</b>同一个店里，送礼的、自用的、买草编包的，理由完全不同；一套话术对三类人都说，等于对谁都不成立。</li>
        </ul>"""
if old_block:
    s = s[: old_block.start()] + new_block + s[old_block.end():]
else:
    print("MISS business block")

# 3) 字号调回
s = s.replace("font-size: 9.2pt; line-height: 1.5;", "font-size: 9.5pt; line-height: 1.56;")

io.open(path, "w", encoding="utf-8").write(s)
print("done; 联合主理人 left:", "联合主理人" in s)
