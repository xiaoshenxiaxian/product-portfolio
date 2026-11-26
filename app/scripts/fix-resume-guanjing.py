# -*- coding: utf-8 -*-
"""两版简历同步观境口径：5→6 个状态；去掉「6 位用户试用」表述。"""
import io

files = [
    r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品助理-素版-2026.html",
    r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-AI产品专员-云智达创-2026.html",
]

for path in files:
    s = io.open(path, encoding="utf-8").read()
    before = s

    s = s.replace("<b>5 个订单状态、4 类异常</b>", "<b>6 个订单状态、4 类异常</b>")
    s = s.replace("；6 位用户试用后主链路从 <b>5 步砍到 3 步</b>。", "；主链路从 <b>5 步砍到 3 步</b>。")
    s = s.replace("；6 位用户试用后主链路从 <b>5 步砍到 3 步</b>", "；主链路从 <b>5 步砍到 3 步</b>")

    io.open(path, "w", encoding="utf-8").write(s)
    print(path.split("\\")[-1], "changed:", s != before, "| 5 个 left:", "5 个订单状态" in s, "| 6 位 left:", "6 位用户" in s)
