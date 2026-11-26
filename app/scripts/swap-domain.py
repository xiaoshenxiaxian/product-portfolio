# -*- coding: utf-8 -*-
"""把所有简历与站点里的旧域名替换为 shenjunhui.cn。"""
import io
import os

OLD = "shenjunhui-news.surge.sh"
NEW = "shenjunhui.cn"

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理"
DIRS = [
    BASE + r"\产品助理\新产品助理",
    BASE + r"\作品\简历修改\作品集修改\homepage\public\resume",
]

changed = []
for d in DIRS:
    for name in os.listdir(d):
        if not name.endswith((".html", ".md", ".txt", ".json")):
            continue
        p = os.path.join(d, name)
        try:
            s = io.open(p, encoding="utf-8").read()
        except Exception:
            continue
        if OLD in s:
            io.open(p, "w", encoding="utf-8").write(s.replace(OLD, NEW))
            changed.append(name)

print("replaced in", len(changed), "files")
for c in sorted(changed):
    print(" -", c)
