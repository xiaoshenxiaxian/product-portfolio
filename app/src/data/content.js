// 首页：第一屏是实习项目（在线住宿 / 订单管理，可切换），其余作品沿弧线排列。
// 所有数字只来自简历与真实素材。

export const nav = {
  links: [
    { label: '实习', href: '#top' },
    { label: '作品', href: '#works' },
    { label: '底子', href: '#grounding' },
    { label: '关于', href: '#about' },
  ],
  pills: [
    { icon: 'intern', label: '实习', href: '#top' },
    { icon: 'works', label: '作品', href: '#works' },
    { icon: 'ground', label: '底子', href: '#grounding' },
    { icon: 'about', label: '关于', href: '#about' },
    { icon: 'resume', label: '简历', href: '/resume/' },
  ],
  resume: { label: '简历', href: '/resume/' },
}

export const hero = {
  roleLabel: '求职方向',
  roleValue: '产品助理',
  meta: '2026 届 · 深圳 / 广州 / 杭州 · 可随时到岗',
  title: '在线住宿与订单管理',
  kicker: '实习 · 某文旅数字化服务商 · 2026.03 – 2026.05',
  caseHref: '/work/huoliyuan.html',
  tabs: [
    {
      id: 'stay',
      label: '住宿预订',
      sub: '详情页和订单页是我独立改的：先把信息顺序定下来，再动界面。哪些字段必须在第一屏、哪一步可以合并，都写进了 PRD。',
      facts: [
        { n: '2 个', label: '核心页面迭代' },
        { n: '8 页', label: 'PRD' },
        { n: '2 个月', label: '实习期' },
      ],
      doc: {
        src: '/work/prd-2.webp',
        alt: 'PRD 第 2 页：需求目标与名词定义',
        tab: 'PRD · 目标与定义',
      },
    },
    {
      id: 'order',
      label: '订单管理',
      sub: '订单状态散落、没认证就发起支付、对账靠人工——用状态机、认证前置和回调幂等，把从下单到退款的主链路打通。',
      facts: [
        { n: '6 个', label: '订单状态' },
        { n: '5 类', label: '支付异常' },
        { n: '8 页', label: 'PRD' },
      ],
      doc: {
        src: '/work/prd-3.webp',
        alt: 'PRD 第 3 页：角色权限、业务流程与订单状态机',
        tab: 'PRD · 订单状态机',
      },
    },
  ],
  cta: '进入案例',
}

export const works = {
  label: '作品',
  title: '另外六个项目',
  lede: '沿这条弧线挑一个，点开是完整拆解。',
  items: [
    {
      id: 'yuexi',
      name: '月汐 · 树洞',
      kicker: 'AI 情绪陪伴',
      thumb: '/work/moontide-1.webp',
      alt: '月汐·树洞原型首页：问候、经期提示与情绪选择',
    },
    {
      id: 'zhuaban',
      name: '爪伴 · 同城领养',
      kicker: '信任机制',
      thumb: '/work/pawbei-1.webp',
      alt: '爪伴同城领养原型首页：待领养宠物与筛选',
    },
    {
      id: 'zhilan',
      name: '知澜 · 在线教育',
      kicker: '留存机制',
      thumb: '/work/zhilan-1.webp',
      alt: '知澜在线教育原型首页：课程与学习进度',
    },
    {
      id: 'guanjing',
      name: '观境 · 文旅',
      kicker: '交易闭环',
      thumb: '/work/guanying-1.webp',
      alt: '观境文旅原型首页：目的地与活动入口',
    },
    {
      id: 'desktop',
      name: '桌面美化 · 订阅',
      kicker: '商业化诊断',
      thumb: '/work/desktop-1.webp',
      alt: '桌面美化原型浏览页：不常驻付费浮层',
    },
    {
      id: 'agent',
      name: '需求拆解 Agent',
      kicker: 'Dify 工作流',
      thumb: '/work/agent-cover.webp',
      alt: '需求拆解 Agent 封面：用户输入 → 知识检索 → LLM → 输出',
    },
  ],
}

export const grounding = {
  label: '底子',
  title: '做产品之前，我在店里站了 15 个月',
  lede: '家乡特产与手工艺品小店，2022–2026 的节假日，累计 15 个月。选品、定价、陈列、备货、算账，都是我自己盯的。',
  stats: [
    { n: '15 个月', label: '累计门店 · 2022–2026（节假日）' },
    { n: '28–75 岁', label: '客群跨度' },
    { n: '3 套', label: '陈列与话术' },
  ],
  audience: {
    rows: [
      ['28–55 岁 · 送礼', '体面、拿得出手', '礼盒装，包装与话术一起改'],
      ['55 岁以上 · 自用', '实在、划算', '实惠装，分量与性价比优先'],
      ['20–70 岁 · 草编包', '出片 / 格调 / 耐用', '三套陈列，讲不同的重点'],
    ],
  },
}

export const about = {
  label: '关于',
  title: '关于我',
  text: '计算机背景，2026 届。在店里累计做过 15 个月运营，也在一家数字科技公司做过产品助理实习。能自己把想法做成原型，也愿意做那些不出彩但必须落地的活。',
  contacts: [
    { k: '邮箱', v: '18759103296@163.com', href: 'mailto:18759103296@163.com' },
    { k: '电话', v: '18759103296', href: 'tel:18759103296' },
    { k: '城市', v: '深圳 / 广州 / 杭州（可接受现场办公）' },
    { k: '到岗', v: '可随时到岗' },
    { k: '学历', v: '阳光学院 · 计算机科学与技术（本科）', meta: '2024.09–2026.06' },
    { k: '前段', v: '湄洲湾职业技术学院 · 计算机应用技术（专科）', meta: '2021.09–2024.06' },
  ],
  intent: '在找产品助理的机会，深圳 / 广州 / 杭州优先。',
  closing: ['先把问题拆清楚，', '再动手做出来。'],
}
