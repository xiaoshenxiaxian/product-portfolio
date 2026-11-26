# -*- coding: utf-8 -*-
"""统一试用人数为 12 人：月汐 6→12，观境补上 12 位试用者。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()
before = s

# 月汐：6 位 → 12 位
s = s.replace(
    "局限：6 位用户试用，没有线上数据",
    "局限：12 位用户试用，没有线上数据",
)

# 观境：交付与复盘补一条（与简历、README 口径一致）
old = """          'C 端 10 个页面 + B 端 5 个模块，C / B 共用一套订单状态语言，改一处不用改 10 页；交付页面清单、字段表、权限矩阵、配置清单、验收清单。',"""
new = """          'C 端 10 个页面 + B 端 5 个模块，C / B 共用一套订单状态语言，改一处不用改 10 页；交付页面清单、字段表、权限矩阵、配置清单、验收清单。',
          '交付前请 12 位试用者走过一遍原型，反馈集中在「主链路和支线太多」，据此砍掉支线，主链路从 5 步减到 3 步。',"""
if old in s:
    s = s.replace(old, new)
else:
    print("MISS guanjing")

io.open(p, "w", encoding="utf-8").write(s)
print("changed:", s != before)
