# -*- coding: utf-8 -*-
"""给 cases.js 里每个案例加 docs 链接（插在 note 之前）。"""
import io
import re

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
src = io.open(path, encoding="utf-8").read()

DOCS = {
    "huoliyuan": [
        ("脱敏 PRD（PDF，8 页）", "/docs/huoliyuan-order-prd.pdf"),
        ("订单帮助中心（PDF，3 页）", "/docs/order-help-center.pdf"),
    ],
    "yuexi": [("PRD 摘要（PDF，2 页）", "/docs/yuexi-prd.pdf")],
    "zhuaban": [("完整 PRD（PDF，12 页）", "/docs/zhuaban-prd.pdf")],
    "zhilan": [("完整 PRD（PDF，12 页）", "/docs/zhilan-prd.pdf")],
    "guanjing": [("完整 PRD（PDF，16 页）", "/docs/guanjing-prd.pdf")],
    "desktop": [("付费墙 PRD 摘要（PDF，2 页）", "/docs/desktop-prd.pdf")],
    "agent": [("PRD 摘要（PDF，2 页）", "/docs/agent-prd.pdf")],
}

for case_id, items in DOCS.items():
    block_start = src.index(f"  {case_id}: {{")
    note_pos = src.index("\n    note:", block_start)
    if "docs:" in src[block_start:note_pos]:
        print("skip (has docs)", case_id)
        continue
    entries = ",\n".join(
        f"      {{ label: {label!r}, href: {href!r} }}".replace("'", "'")
        for label, href in items
    )
    block = (
        "\n    docs: [\n"
        + ",\n".join(
            "      { label: '%s', href: '%s' }" % (label, href) for label, href in items
        )
        + ",\n    ],"
    )
    src = src[:note_pos] + block + src[note_pos:]
    print("added", case_id, len(items))

io.open(path, "w", encoding="utf-8").write(src)
print("done")
