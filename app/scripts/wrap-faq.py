# -*- coding: utf-8 -*-
"""把 FAQ 每条包进 .qa 容器，避免跨页拆开。"""
import io
import re
import sys

path = sys.argv[1]
html = io.open(path, encoding="utf-8").read()

start = html.index('<div class="faq">')
end = html.index("客服查不到订单")
end = html.index("</div>", end)
inner = html[start:end]
head = '<div class="faq">'
body = inner[len(head):]

parts = [x for x in re.split(r'(?=<h3><span class="q">)', body) if x.strip()]
wrapped = "".join('<div class="qa">' + x.rstrip() + "</div>\n" for x in parts)
html = html[:start] + head + "\n" + wrapped + html[end:]

if ".qa {" not in html:
    html = html.replace(".faq h3 {", ".qa { break-inside: avoid; }\n      .faq h3 {")

io.open(path, "w", encoding="utf-8").write(html)
print("wrapped items:", len(parts))
