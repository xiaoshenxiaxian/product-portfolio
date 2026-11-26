# -*- coding: utf-8 -*-
"""把误插到 stories 里的 agenteval 块，移到 cases 对象末尾。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

start = s.index("\n  agenteval: {")
end = s.rindex("\n\n}")
block = s[start:end].rstrip()
s2 = s[:start] + s[end:]

pos = s2.index("\n}\n\nexport function getCase")
s3 = s2[:pos] + "\n" + block + s2[pos:]

io.open(p, "w", encoding="utf-8").write(s3)
print("moved. cases ends with agenteval:", s3[pos - 40:pos + 20].replace("\n", "|"))
