# -*- coding: utf-8 -*-
"""把评测内容并入 agent 案例，删除独立的 agenteval 案例页。"""
import io

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage"
p = BASE + r"\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

# 1) 取出 agenteval 块并整体删除
start = s.index("\n  agenteval: {")
end = s.index("\n}\n\nexport function getCase")
block = s[start:end]
s = s[:start] + s[end:]

# 2) 从块里提取 sections 内容（去掉外层 id/meta/gallery/docs/note/intro）
sec_start = block.index("    sections: [")
sec_end = block.index("    gallery: [],")
sections_body = block[sec_start + len("    sections: [\n"): sec_end].rstrip()
# 去掉结尾的 "    ],"
sections_body = sections_body.rstrip()
if sections_body.endswith("],"):
    sections_body = sections_body[:-2].rstrip()

# 3) 追加到 agent 案例的 sections 末尾（在 gallery 前）
agent_pos = s.index("  agent: {")
gal = s.index("\n    gallery: [", agent_pos)
s = s[:gal] + ",\n" + sections_body + s[gal:]

# 4) caseOrder 去掉 agenteval
s = s.replace(", 'agenteval']", "]")

# 5) agent 的 docs 里加两个评测附件，去掉页面链接
s = s.replace(
    "      { label: '评测记录（19/30 → 29/30）', href: '/work/agent-eval.html' },",
    "      { label: '评测集（30 条 + 判定 + 版本对比）', href: '/docs/eval-set.pdf' },\n"
    "      { label: '评测结果（29/30 原始输出）', href: '/docs/eval-final.pdf' },",
)

io.open(p, "w", encoding="utf-8").write(s)
print("agenteval removed:", "agenteval" not in s)
print("eval docs added:", "eval-set.pdf" in s)
