# -*- coding: utf-8 -*-
"""修正 GitHub 用户名：旧写法（含错的 xiaoshenxianxian）统一改为 shenjunhui-pm。"""
import io
import os

OLD = ["xiaoshenxianxian", "xiaoshenxiaxian"]
NEW = "shenjunhui-pm"

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理"
DIRS = [
    BASE + r"\产品助理\新产品助理",
    BASE + r"\作品\简历修改\作品集修改\homepage\public",
    BASE + r"\作品\简历修改\作品集修改\homepage\src",
]

changed = []
for d in DIRS:
    for root, _, files in os.walk(d):
        for name in files:
            if not name.endswith((".html", ".js", ".vue", ".json", ".md")):
                continue
            p = os.path.join(root, name)
            try:
                s = io.open(p, encoding="utf-8").read()
            except Exception:
                continue
            t = s
            for o in OLD:
                t = t.replace(o, NEW)
            if t != s:
                io.open(p, "w", encoding="utf-8").write(t)
                changed.append(p.replace(BASE + "\\", ""))

print("changed:", len(changed))
for c in changed:
    print(" -", c)
