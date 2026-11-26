# -*- coding: utf-8 -*-
"""商业实践改成 FDE 语言：需求拆解 → 场景落地 → 价值验证。"""
import io

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI管培生-蓝凌-2026.html"
s = io.open(path, encoding="utf-8").read()
before = s

old1 = "<li>算清每一笔账：自己盯进货、定价、压货——卖不动的要降价清，压久了就是亏，才知道「库存」不是报表上的数字。</li>"
new1 = "<li>先问清是哪类客人：客人说「随便看看」，真问下去才知道是送礼还是自用——送礼看体面，自用算性价比，同一个问题对应两套说法。</li>"

old2 = "<li>拆开看客人：同一个店里，送礼的、自用的、买草编包的，理由完全不同；一套话术对三类人都说，等于对谁都不成立。</li>"
new2 = "<li>改完第二天就知道对没对：按这三类人调陈列和话术，用动销率判断哪类补货、哪类清仓；卖不动就降价，压货就是亏。</li>"

for old, new in ((old1, new1), (old2, new2)):
    if old not in s:
        print("MISS:", old[:20])
    s = s.replace(old, new)

io.open(path, "w", encoding="utf-8").write(s)
print("changed:", s != before)
