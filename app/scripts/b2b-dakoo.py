# -*- coding: utf-8 -*-
"""达酷版改为 B 端导向：砍月汐、加强观境后台、加串场句。"""
import io
import re

path = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品助理-达酷互动-2026.html"
s = io.open(path, encoding="utf-8").read()

# 1) 删掉月汐整个 entry
m = re.search(r'\n      <div class="entry">\n        <div class="row">\n          <span>月汐.*?</div>\n      </div>', s, re.S)
if m:
    s = s[: m.start()] + s[m.end():]
else:
    print("MISS yuexi block")

# 2) 项目经历下加串场句
s = s.replace(
    '<h2>项目经历</h2>\n      <div class="entry">',
    '<h2>项目经历</h2>\n      <p class="lead">两个项目都是 B 端后台：多角色、权限、流程、验收。</p>\n\n      <div class="entry">',
)

# 3) 观境加强 B 端
s = s.replace(
    "<li><b>跟完 0-1：</b>梳理门票从浏览到核销的流程，定 <b>6 个状态</b>和每个状态下能做什么，输出页面清单、字段表、权限边界与验收清单。</li>",
    "<li><b>跟完 0-1：</b>梳理门票从浏览到核销的流程，定 <b>6 个状态</b>和每个状态下能做什么；<b>C 端 10 页 + B 端 5 个模块</b>共用一套状态语言，改一处不用改十页。</li>",
)
s = s.replace(
    "<li><b>拿真人验证：</b>邀请 <b>12 位试用者</b>走原型，反馈「主链路和支线太多」；据此砍掉分支，主链路从 5 步减到 3 步。</li>",
    "<li><b>交付与验证：</b>输出页面清单、字段表、<b>四种角色的权限边界</b>、配置与验收清单；邀请 <b>12 位试用者</b>走原型，砍掉多余支线，主链路从 5 步减到 3 步。</li>",
)

# 4) 摘要改成 B 端口吻
s = s.replace(
    "计算机 2026 届。跟过一个票务系统从需求到原型的 <b>0-1 过程</b>：定状态、画页面、找 <b>12 位试用者</b>来点、再砍到 3 步；也独立写过 8 页订单支付 PRD。会用 Dify 搭 <b>AI 工作流</b>，原型直接用 HTML 做成能点的。",
    "计算机 2026 届。跟过一个票务系统从需求到原型的 <b>0-1 过程</b>：定状态、画页面、找 <b>12 位试用者</b>来点；也独立写过 8 页订单支付 PRD，跟研发联调到字段与权限。会用 Dify 搭 <b>AI 工作流</b>，原型直接用 HTML 做成能点的。",
)

# 5) 串场句样式
s = s.replace(
    ".entry { margin-top: 7px; }",
    ".entry { margin-top: 7px; }\n      .lead { margin: 2px 0 0; font-size: 9pt; color: #4a4f57; }",
)

io.open(path, "w", encoding="utf-8").write(s)
print("月汐 left:", "月汐" in s)
