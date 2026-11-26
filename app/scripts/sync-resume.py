# -*- coding: utf-8 -*-
"""把素版简历同步到作品集：/resume/ 预览页 + /resume.pdf。"""
import os
import shutil

SRC = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品助理-素版-2026.html"
PDF = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\产品助理\新产品助理\沈俊辉-产品助理-素版-2026.pdf"
DST = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\public\resume"

BAR = """
<div class="rv-bar">
  <a href="/">← 返回作品集</a>
  <a class="rv-dl" href="/resume.pdf">下载 PDF</a>
</div>
<style>
  .rv-bar {
    position: fixed;
    right: 18px;
    bottom: 18px;
    z-index: 99;
    display: flex;
    gap: 8px;
    font: 500 12.5px/1 "Noto Sans SC", "PingFang SC", system-ui, sans-serif;
    letter-spacing: .04em;
  }
  .rv-bar a {
    padding: 10px 16px;
    border: 1px solid rgba(21, 23, 27, .22);
    border-radius: 999px;
    background: #F7F4ED;
    color: #15171B;
    text-decoration: none;
    transition: background .2s, color .2s, border-color .2s;
  }
  .rv-bar a:hover { background: #15171B; border-color: #15171B; color: #F7F4ED; }
  .rv-dl { border-color: rgba(21, 23, 27, .45); }
  @media print { .rv-bar { display: none } }
</style>
"""


def main():
    os.makedirs(DST, exist_ok=True)
    html = open(SRC, encoding="utf-8").read()
    if "</body>" not in html:
        raise SystemExit("no </body>")
    html = html.replace("</body>", BAR + "</body>", 1)
    open(os.path.join(DST, "index.html"), "w", encoding="utf-8").write(html)
    photo_src = os.path.join(os.path.dirname(SRC), "photo.webp")
    if os.path.exists(photo_src):
        shutil.copyfile(photo_src, os.path.join(DST, "photo.webp"))
        print("copied photo.webp")
    shutil.copyfile(PDF, os.path.join(DST, "..", "resume.pdf"))
    print("wrote", os.path.join(DST, "index.html"))
    print("copied resume.pdf", os.path.getsize(os.path.join(DST, "..", "resume.pdf")), "bytes")


main()
