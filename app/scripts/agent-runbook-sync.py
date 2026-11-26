# -*- coding: utf-8 -*-
"""Agent 案例页：更新测试口径、补运行手册小节与附件。"""
import io

p = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

# 1) 旧的 6 条用例小节改名
s = s.replace(
    "        h: '测试：6 条用例，实测 5 条',",
    "        h: '起步：手动跑 6 条，先确认它能跑',",
)

# 2) 在评测小节前加一段过渡
bridge = """      {
        h: '6 条不够：只证明它能跑，不证明它靠得住',
        paras: [
          '手动跑 6 条，能确认「八段能出全」「该拒的时候会拒」。但它回答不了一个问题：改一版提示词，整体是变好了还是变差了？',
          '所以后面又做了 30 条评测集——6 类是「应该成功」，还有 11 条是「应该失败」。下面几节就是那轮的完整记录。',
        ],
      },
"""
s = s.replace("      {\n        h: '为什么给一个 Agent 做评测',", bridge + "      {\n        h: '为什么给一个 Agent 做评测',")

# 3) 结尾补「运行手册」小节
runbook = """      {
        h: '运行手册：别人接手时先看这一页',
        bullets: [
          '它做什么、不做什么：一句话说清边界（不生成页面、不承诺工期、不替客户定目标值）。',
          '坏了怎么修：输出带 <think> / 输出是 JSON 串 / 该出方案却只提问 / 批量失败，四条现象对应四种处理。',
          '改版怎么回滚：改前记通过率、一次只改一处、降了就回滚到上一版提示词。',
          '成本与限流：单次约 3–4 万 tokens，缓存命中 99.6%；30 条批量会撞 Dify 知识库检索配额，改每批 10 条。',
        ],
        paras: ['手册 2 页，交接时连评测集、提示词版本、知识库 6 篇一起给。'],
      },
"""
s = s.replace("      {\n        h: '方法：每轮只改一个变量',", runbook + "      {\n        h: '方法：每轮只改一个变量',")

# 4) 附件
s = s.replace(
    "      { label: '评测结果（29/30 原始输出）', href: '/docs/eval-final.pdf' },",
    "      { label: '评测结果（29/30 原始输出）', href: '/docs/eval-final.pdf' },\n"
    "      { label: '运行手册（2 页）', href: '/docs/agent-runbook.pdf' },",
)

io.open(p, "w", encoding="utf-8").write(s)
print("test renamed:", "起步：手动跑 6 条" in s)
print("runbook section:", "运行手册：别人接手时先看这一页" in s)
print("runbook doc:", "agent-runbook.pdf" in s)
