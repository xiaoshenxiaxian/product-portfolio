# -*- coding: utf-8 -*-
"""把 Agent 评测页接入站点：新增 case 数据、路由、vite 入口。"""
import io

BASE = r"D:\沈俊辉\简历\new\简历1\电商运营简历最新版\AI产品运营助理\作品\简历修改\作品集修改\homepage"

# 1) cases.js：加数据 + 加 caseOrder
p = BASE + r"\src\data\cases.js"
s = io.open(p, encoding="utf-8").read()

s = s.replace(
    "export const caseOrder = ['huoliyuan', 'yuexi', 'zhuaban', 'zhilan', 'guanjing', 'desktop', 'agent']",
    "export const caseOrder = ['huoliyuan', 'yuexi', 'zhuaban', 'zhilan', 'guanjing', 'desktop', 'agent', 'agenteval']",
)

entry = """
  agenteval: {
    id: 'agenteval',
    no: '08',
    name: '需求拆解 Agent · 评测',
    kicker: '个人项目 · 评测与迭代',
    sub: '30 条评测集，第一次只过 19 条。两轮迭代到 29 条——这里记录每一步改了什么、为什么改，以及那条至今没过的用例。',
    meta: [
      { k: '角色', v: '独立完成（评测设计 + 迭代）' },
      { k: '时间', v: '2026.11' },
      { k: '范围', v: '30 条 / 7 类场景 / 3 版迭代' },
      { k: '交付', v: '评测集 · 原始输出 · 版本对比' },
    ],
    sections: [
      {
        h: '为什么给一个 Agent 做评测',
        paras: [
          '写个提示词就能跑出像样的结果，但「像样」和「能用」是两件事。没有评测集，改一版提示词只能凭感觉说「好像好点了」。',
          '所以先建 30 条评测集，把第一次的结果当基线，再一轮一轮改。这个页面记录完整过程——包括没改好的那一轮。',
        ],
      },
      {
        h: '评测集：7 类场景，30 条',
        table: {
          head: ['类型', '条数', '在测什么'],
          rows: [
            ['完整场景', '8', '正常输入能不能出八段方案'],
            ['模糊需求', '6', '该追问时会不会硬编'],
            ['角色冲突', '4', '会不会只站一边'],
            ['知识库无覆盖', '4', '会不会编造字段与指标'],
            ['多诉求 / 超长', '4', '会不会混成一份方案'],
            ['无关输入', '3', '会不会答非所问'],
            ['敏感', '1', '会不会越界采集'],
          ],
        },
        paras: ['关键设计：里面故意放了 11 条「应该失败」的用例。一个只跑正常 case 的评测集，说明不了任何事。'],
      },
      {
        h: '基线：19/30，两个不同的问题',
        bullets: [
          '格式问题（0/30 可读）：输出里带着思考过程，外层包着 JSON，换行被转义成 \\\\n——别人拿到这个应用，第一眼就是不可用。',
          '策略问题（A 类 0/8）：8 条信息完整的用例，全部只输出「待确认清单」。它有症状、有两个角色、有业务背景，却一条方案都不给。',
        ],
        paras: [
          'A01 的真实输出：「输入仅一句客户原话……以下不补齐事实。## 待确认清单（先列）」，后面八段全标「待确认」。',
        ],
      },
      {
        h: '第一轮：先修格式，A 类从 0 到 8',
        paras: [
          '打开推理标签分离、把结束节点的输出从「整个节点对象」改成 text 字段、加一个代码节点清洗；提示词从「信息不足就提问」改成打分制——四项打分，≥3 分必须出方案。',
          '结果 24/30。A 类 8/8，但 C 类从 4/4 掉到 2/4：门槛定太死，只有一个角色的需求被判成「信息不足」。',
        ],
      },
      {
        h: '第二轮：放宽门槛，29/30',
        paras: [
          '角色门槛从「≥2 个」降到「≥1 个」；多诉求单独加 1 分；合规敏感类单独给规则（风险 + 最小化建议 + 一个待确认）。',
          '结果 29/30。C 类回到 4/4，E 类从 1/4 到 3/4。',
        ],
      },
      {
        h: '三版对比',
        table: {
          head: ['类型', 'v1 基线', 'v3.1', 'v3.2'],
          rows: [
            ['完整场景', '0/8', '8/8', '8/8'],
            ['模糊需求', '6/6', '6/6', '6/6'],
            ['角色冲突', '4/4', '2/4', '4/4'],
            ['知识库无覆盖', '4/4', '4/4', '4/4'],
            ['多诉求 / 超长', '1/4', '1/4', '3/4'],
            ['无关输入', '3/3', '3/3', '3/3'],
            ['敏感', '1/1', '0/1', '1/1'],
            ['合计', '19/30', '24/30', '29/30'],
          ],
        },
      },
      {
        h: '留下的那一条失败',
        paras: [
          'E03「既要批量导入，又要能导出，还要对接现有 ERP」被判 1 分，只给待确认清单。原因是我的业务对象清单里没有「后台模块」这一类。',
          '没有修。29/30 已经说明问题，留一条已知边界比做满 100% 更可信——我知道它在哪里会失手。',
        ],
      },
      {
        h: '方法：每轮只改一个变量',
        bullets: [
          '同一套 30 条题，每轮都重跑一遍，不换题；',
          '一次只改一处（先格式，后策略），改完才知道是谁带来的变化；',
          '失败要归因：Dify 知识库检索有速率限制，批量跑会失败几条——这类记「环境问题」，不算进模型指标。',
        ],
      },
    ],
    gallery: [],
    docs: [
      { label: '评测集（30 条 + 判定）', href: '/docs/eval-set.pdf' },
      { label: '基线结果（19/30）', href: '/docs/eval-baseline.pdf' },
      { label: '最终结果（29/30）', href: '/docs/eval-final.pdf' },
    ],
    note: '个人项目，未上线；评测为本人执行，样本 30 条，不是大规模评测。',
    intro: [
      {
        act: '08 / EVAL',
        title: '一个 Agent 的评测记录',
        text: '30 条题，19 → 24 → 29。记录每一步改了什么、为什么改，以及那条没过的用例。',
      },
    ],
  },
"""

# 插入到 cases 对象结尾之前
idx = s.rstrip().rfind("\n}")
s = s[:idx] + "\n" + entry + s[idx:]
io.open(p, "w", encoding="utf-8").write(s)
print("cases.js ok | agenteval:", "agenteval:" in s)

# 2) vite.config.js：加入口
vp = BASE + r"\vite.config.js"
v = io.open(vp, encoding="utf-8").read()
if "work/agent-eval.html" not in v:
    v = v.replace(
        "        agent: resolve(import.meta.dirname, 'work/agent.html'),",
        "        agent: resolve(import.meta.dirname, 'work/agent.html'),\n        'agent-eval': resolve(import.meta.dirname, 'work/agent-eval.html'),",
    )
    io.open(vp, "w", encoding="utf-8").write(v)
print("vite ok |", "agent-eval" in io.open(vp, encoding="utf-8").read())
