# AI产品概念扫盲 - 视频完整规格拆解

> 本文档逐像素、逐帧拆解视频的每个元素。只要提供文案内容，按本规格填充即可生成风格一致的视频。

---

## 一、全局基础规格

| 项目 | 规格 |
|------|------|
| 分辨率 | 2400×3200px (3:4竖版) |
| FPS | 25 |
| 视频编码 | H.264 High Profile Level 5.1 |
| 音频 | AAC 192k 48kHz mono |
| 字体 | Noto Sans SC (300/400/500/700/900) |
| GSAP版本 | 3.12.5 (CDN) |
| 渲染方式 | Playwright headless Chromium 逐帧截图 |

### 1.1 背景系统

```
body 背景: #050810 (纯深色)
#stage 背景: radial-gradient(ellipse at 50% 40%, #0F172A 0%, #050810 80%)
```
效果：从画面中心偏上(50%,40%)向外，深蓝灰(#0F172A)渐变到近黑(#050810)。

### 1.2 颜色系统

| 色名 | 色值 | 用途 |
|------|------|------|
| 主色-青绿 | `#00D4AA` | 进度条起始、主标签、高亮、正面强调 |
| 蓝 | `#3B82F6` | 偏见/开发类元素 |
| 紫 | `#A855F7` | 沟通/创意类元素 |
| 橙 | `#F59E0B` | 进度条末尾、商业/注意类元素 |
| 绿 | `#22C55E` | 协作/运维/优势类元素 |
| 红粉 | `#FF6B6B` | 负面/不适合类元素 |
| 青蓝 | `#22D3EE` | 品牌标签专用 |
| 白 | `#FFFFFF` | 主标题文字 |
| 浅灰 | `#94A3B8` | 副文本、描述文字 |
| 深蓝灰 | `#1E293B` | 卡片底色 |
| 暗红 | `#8B1E3F` | 刻板印象标签底色 |
| 浅文字 | `#E2E8F0` | 卡片内引用文字 |
| 底卡文字 | `#1F2937` | 底部白色卡片内文字 |

### 1.3 全局固定组件

#### 进度条 (始终显示)
```css
位置: top:0; left:0; right:0; 高度:6px
背景: rgba(255,255,255,0.05)
填充: linear-gradient(90deg, #00D4AA, #F59E0B), 圆角0 4px 4px 0
z-index: 100
```

#### 右上角标签 (始终显示)
```css
位置: top:30px; right:40px
样式: 胶囊形(border-radius:999px)
背景: rgba(0,212,170,0.15)
边框: 1px solid rgba(0,212,170,0.4)
文字: color:#00D4AA; font-size:22px; font-weight:500; letter-spacing:1px
内容格式: "[系列名] [主题] | 第N课 ★ 深度解析"
★符号: color:#F59E0B
z-index: 50
```

#### 底部白色卡片 (每个场景都有)
```css
位置: bottom:0; 满宽
背景: #FFFFFF
圆角: 32px 32px 0 0 (仅上方圆角)
内边距: padding: 50px 80px 70px 80px
最小高度: 480px
文字: font-size:42px; font-weight:700; color:#1F2937; line-height:1.7; text-align:center
垂直居中: display:flex; align-items:center; justify-content:center
```

#### 字幕条 (每个场景都有)
```css
位置: bottom:500px; 水平居中(left:50%; transform:translateX(-50%))
背景: rgba(0,0,0,0.7) + backdrop-filter:blur(10px)
圆角: 12px
内边距: 16px 40px
最大宽度: 1800px
文字: font-size:36px; font-weight:600; color:#FFFFFF; text-align:center
初始: opacity:0
激活: .active { opacity:1 }
过渡: transition:opacity 0.2s
z-index: 80
```

#### 内容区域 (每个场景的主体内容区)
```css
位置: absolute; top:80px; left:0; right:0; bottom:480px
Flex布局: column; align-items:center; justify-content:center
内边距: padding: 0 100px
```

---

## 二、场景逐个拆解

### 场景1：开场引入 (0 - 8.35s)

#### 2.1.1 布局结构
```
content-area (垂直居中)
├── icon-matrix (2×2网格, 500×500px, gap:24px)
│   ├── icon-cell.c1 (青绿 #00D4AA) — 代码图标
│   ├── icon-cell.c2 (绿色 #22C55E) — 人物图标
│   ├── icon-cell.c3 (橙色 #F59E0B) — 公文包图标
│   └── icon-cell.c4 (紫色 #A855F7) — 网络图标
├── main-title (72px, 白色, 900)
├── gradient-subtitle (48px, 700, 三色渐变)
└── tag-row (flex, gap:30px)
    ├── tag-left (胶囊标签, 青绿)
    └── tag-right (描述文字, 灰色)
```

#### 2.1.2 图标格子规格
```css
尺寸: 各占1/4, gap:24px
背景: rgba(30,41,59,0.7) + blur(20px)
边框: 1px solid rgba(255,255,255,0.06)
圆角: 24px
阴影: box-shadow: 0 8px 32px rgba(0,0,0,0.3)
SVG: 72×72px, stroke-width:1.8, fill:none
```

#### 2.1.3 渐变副标题
```css
font-size:48px; font-weight:700
background: linear-gradient(90deg, #00D4AA 0%, #00B4D8 50%, #FFD700 100%)
-webkit-background-clip: text; -webkit-text-fill-color: transparent
margin-top: 20px
```

#### 2.1.4 SVG图标代码
- c1 代码: `<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>`
- c2 人物: `<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>`
- c3 公文包: `<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><line x1="3" y1="13" x2="21" y2="13"/>`
- c4 网络: `<circle cx="12" cy="12" r="3"/><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>` + 4条连线

#### 2.1.5 动画时间线
| 时间 | 元素 | 动画 | 参数 |
|------|------|------|------|
| 0.00s | scene1 | set visible | opacity:1, visibility:visible |
| 0.09s | icon-cell ×4 | 缩放弹入 | scale:0→1, opacity:0→1, stagger:0.15, duration:0.4, ease:back.out(1.7) |
| 0.43s | main-title | 上滑入 | y:40→0, opacity:0→1, duration:0.5 |
| 0.61s | gradient-subtitle | 上滑入 | y:30→0, opacity:0→1, duration:0.5 |
| 0.78s | tag-row | 上滑入 | y:20→0, opacity:0→1, duration:0.4 |
| 0.87s | bottom-card | 上滑入 | y:100→0, opacity:0→1, duration:0.5 |
| 8.05s | scene1 | 淡出 | opacity:1→0, duration:0.3, ease:power2.in |
| 8.35s | scene1 | set hidden | visibility:hidden |

#### 2.1.6 文案模式
```
右上角标签: "[系列名] [主题] | 第N课 ★ 深度解析"
icon-matrix: 4个图标代表概念的4个维度
main-title: 问句格式 "什么人适合做XX?"
gradient-subtitle: 一句话概括（渐变色）
tag-left: 核心标签（如"能力模型剖析"）
tag-right: 副描述（如"拒绝刻板印象，找到你的职业锚点"）
bottom-card: 引入语（约30-50字，制造冲突）
TTS: 与bottom-card内容相同
```

---

### 场景2：刻板印象 vs 真实 (8.35 - 17.58s)

#### 2.2.1 布局结构
```
content-area
├── pill-badge.badge-stereotype (暗红底标签 "STEREOTYPE VS REALITY")
├── main-title (72px, 白色)
└── three-cards (flex, gap:40px, max-width:2200px)
    ├── stereo-card.dimmed (左：偏见一)
    │   ├── icon-row (ico图标 + 卡片标题)
    │   │   ├── .ico (60×60圆角方块, 蓝/红背景)
    │   │   └── .card-title (30px)
    │   └── card-quote ×3 (30px, 浅色文字)
    ├── stereo-card.center (中：真相，高亮)
    │   ├── .card-title (青绿色, 居中)
    │   ├── .card-subtitle (26px, 灰色, 居中)
    │   └── .card-quote ×2 (30px, 居中, 含highlight-text)
    └── stereo-card.dimmed (右：偏见二)
        └── 同左卡片结构
```

#### 2.2.2 卡片规格
```css
通用卡片:
  flex:1; max-width:600px; padding:50px 40px
  border-radius:24px
  background:rgba(30,41,59,0.5)
  border:1px solid rgba(255,255,255,0.06)
  backdrop-filter:blur(20px)

中间高亮卡片(.center):
  border:2px solid #00D4AA
  box-shadow:0 0 40px rgba(0,212,170,0.3)
  background:rgba(0,212,170,0.05)

两侧暗淡卡片(.dimmed):
  opacity:0.3
```

#### 2.2.3 SVG图标代码
- 偏见图标(X叉): `<line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/>`
- 标签底色: 蓝偏见 `rgba(59,130,246,0.2);color:#3B82F6` / 红偏见 `rgba(255,107,107,0.2);color:#FF6B6B`

#### 2.2.4 动画时间线
| 时间 | 元素 | 动画 | 参数 |
|------|------|------|------|
| 8.35s | scene2 | 淡入 | fromTo opacity:0→1, duration:0.2 |
| 8.35s | pill-badge | 下滑入 | y:-30→0, opacity:0→1, duration:0.4 |
| 8.52s | main-title | 上滑入 | y:30→0, opacity:0→1, duration:0.4 |
| 8.61s | stereo-card ×3 | 左右滑入 | x:左-80/中0/右+80→0, opacity:0→1, scale:0.9→1, stagger:0.2, duration:0.5, ease:power2.out |
| 8.96s | bottom-card | 上滑入 | y:100→0, opacity:0→1, duration:0.5 |
| 10.44s | s2-card-center | 发光脉冲 | boxShadow→'0 0 60px rgba(0,212,170,0.5)', duration:0.5, yoyo:true, repeat:1 |
| 17.28s | scene2 | 淡出 | opacity:1→0, duration:0.3, ease:power2.in |
| 17.58s | scene2 | set hidden | visibility:hidden |

#### 2.2.5 文案模式
```
pill-badge: 英文标签（如 "STEREOTYPE VS REALITY"），暗红底
main-title: "关于XX的两大刻板印象"
左卡片: 偏见一名称 + 3条偏见描述（引号包裹）
中卡片: "真正的XX" + 副标题(英文全称) + 2条真相描述（含高亮关键词）
右卡片: 偏见二名称 + 3条偏见描述
bottom-card: 总结真相（约40字）
TTS: 与bottom-card相同
```

---

### 场景3：核心模型/技能条 (17.58 - 30.08s)

#### 2.3.1 布局结构
```
content-area
├── pill-badge.badge-model (深蓝底标签, 含圆点)
├── main-title
└── skill-bars (max-width:1800px)
    └── skill-item ×3 (margin-bottom:50px)
        ├── skill-header (flex, gap:20px)
        │   ├── skill-icon-box (64×64, 圆角16px, SVG 32×32)
        │   ├── skill-name (36px, 700)
        │   └── skill-pct (36px, 700, margin-left:auto)
        ├── skill-track (高24px, 圆角12px, 暗底)
        │   └── skill-fill (width:0%→XX%, 渐变色填充)
        └── skill-desc (26px, 灰色)
```

#### 2.3.2 技能条规格
```css
skill-track: height:24px; background:rgba(51,65,85,0.5); border-radius:12px; overflow:hidden
skill-fill: height:100%; border-radius:12px; width:0%(初始)
颜色对应:
  60%→#00D4AA(青绿), 30%→#A855F7(紫), 10%→#F59E0B(橙)
图标盒子:
  64×64px; border-radius:16px
  背景色: 各色对应的0.2透明度
  SVG: 32×32px; stroke-width:2; fill:none
```

#### 2.3.3 SVG图标代码
- 技术(代码): `<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>`
- 沟通(对话): `<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>`
- 商业(柱状图): `<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>`

#### 2.3.4 动画时间线
| 时间 | 元素 | 动画 | 参数 |
|------|------|------|------|
| 17.58s | scene3 | 淡入 | fromTo opacity:0→1, duration:0.2 |
| 17.58s | pill-badge | 下滑入 | y:-30→0, opacity:0→1, duration:0.4 |
| 17.75s | main-title | 上滑入 | y:30→0, opacity:0→1, duration:0.4 |
| 17.85s | skill-icon-box ×3 | 旋转弹入 | rotation:-15→0, scale:0.8→1, opacity:0→1, stagger:0.3, duration:0.4, ease:back.out(1.7) |
| 17.85s | skill-item ×3 | 上滑入 | y:50→0, opacity:0→1, stagger:0.3, duration:0.5 |
| 18.28s | bar1 | 填充 | width:0→60%, duration:0.8, ease:power2.out |
| 18.62s | bar2 | 填充 | width:0→30%, duration:0.6, ease:power2.out |
| 18.88s | bar3 | 填充 | width:0→10%, duration:0.4, ease:power2.out |
| 19.06s | bottom-card | 上滑入 | y:100→0, opacity:0→1, duration:0.5 |
| 29.78s | scene3 | 淡出 | opacity:1→0, duration:0.3, ease:power2.in |
| 30.08s | scene3 | set hidden | visibility:hidden |

#### 2.3.5 文案模式
```
pill-badge: 英文模型名（如 "The 6-3-1 Model"）, 含圆点指示器
main-title: "XX黄金技能模型：60-30-10"
skill-item ×3:
  - 技能名 + 百分比 + 图标 + 一行描述
  - 按百分比从大到小排列
bottom-card: 总结模型（约50字，含具体百分比）
TTS: 与bottom-card相同
```

---

### 场景4：人群诊断/对比 (30.08 - 40.59s)

#### 2.4.1 布局结构
```
content-area
├── pill-badge.badge-traits (绿色标签, 含圆点 "Traits Checklist")
├── main-title
└── dual-cards (flex, gap:50px, max-width:2200px)
    ├── trait-card.good (左：适合)
    │   ├── card-icon (72×72圆形, 青绿背景, SVG 36×36)
    │   ├── card-title (38px, 青绿色)
    │   └── trait-item ×3
    │       ├── item-icon (48×48, 圆角12px, SVG 24×24)
    │       └── item-content
    │           ├── item-title (30px, 白色)
    │           └── item-desc (24px, 灰色)
    └── trait-card.bad (右：不适合)
        └── 同左结构, 红粉色系
```

#### 2.4.2 卡片规格
```css
good卡片:
  border:2px solid rgba(0,212,170,0.4)
  background:rgba(0,212,170,0.05)
  box-shadow:0 0 30px rgba(0,212,170,0.15)

bad卡片:
  border:2px solid rgba(255,107,107,0.4)
  background:rgba(255,107,107,0.05)
  box-shadow:0 0 30px rgba(255,107,107,0.15)

card-icon:
  72×72px; border-radius:50%
  good: background:rgba(0,212,170,0.2); color:#00D4AA
  bad: background:rgba(255,107,107,0.2); color:#FF6B6B
  SVG: 36×36px; stroke-width:2.5

item-icon:
  48×48px; border-radius:12px
  good: background:rgba(0,212,170,0.15); color:#00D4AA
  bad: background:rgba(255,107,107,0.15); color:#FF6B6B
  SVG: 24×24px; stroke-width:2
```

#### 2.4.3 SVG图标代码
- good card-icon(勾): `<polyline points="20 6 9 17 4 12"/>`
- bad card-icon(X): `<line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/>`
- good item1(扳手): `<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>`
- good item2(盾牌): `<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>`
- good item3(飞机): `<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5-.3.5-.2 1.1.3 1.6L9 12l-4 4-3-.5L1 17l3 1 1 3 1.5-1L6 17l4-4 3.7 4.9c.5.5 1.1.6 1.6.3.4-.2.6-.6.5-1z"/>`
- bad item1(代码): `<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>`
- bad item2(禁止): `<circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>`
- bad item3(时钟): `<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>`

#### 2.4.4 动画时间线
| 时间 | 元素 | 动画 | 参数 |
|------|------|------|------|
| 30.08s | scene4 | 淡入 | fromTo opacity:0→1, duration:0.2 |
| 30.08s | pill-badge | 下滑入 | y:-30→0, opacity:0→1, duration:0.4 |
| 30.25s | main-title | 上滑入 | y:30→0, opacity:0→1, duration:0.4 |
| 30.35s | trait-card.good | 左滑入 | x:-80→0, opacity:0→1, duration:0.5, ease:power2.out |
| 30.35s | trait-card.bad | 右滑入 | x:80→0, opacity:0→1, duration:0.5, ease:power2.out |
| 30.60s | trait-item ×6 | 逐项stagger | y:30→0, opacity:0→1, stagger:0.1, duration:0.3 |
| 31.30s | bottom-card | 上滑入 | y:100→0, opacity:0→1, duration:0.5 |
| 40.29s | scene4 | 淡出 | opacity:1→0, duration:0.3, ease:power2.in |
| 40.59s | scene4 | set hidden | visibility:hidden |

#### 2.4.5 文案模式
```
pill-badge: 英文标签（如 "Traits Checklist"）
main-title: "性格诊断：你适合吗？"
good卡片:
  card-icon: 勾号
  card-title: "天选XX体质"
  trait-item ×3: 标题(引号修饰) + 一行描述
bad卡片:
  card-icon: X叉
  card-title: "建议避坑体质"
  trait-item ×3: 标题(引号修饰) + 一行描述
bottom-card: 总结适合/不适合（约40字）
TTS: 与bottom-card相同
```

---

### 场景5：转型路径/实践建议 (40.59 - 51.10s)

#### 2.5.1 布局结构
```
content-area
├── pill-badge.badge-career (深蓝标签, 含蓝圆点 "Career Shift")
├── main-title
└── transition-cards (纵向排列, gap:30px, max-width:2000px)
    └── trans-card ×3 (横向flex布局)
        ├── trans-icon-box (80×80, 圆角20px, SVG 40×40)
        └── trans-content
            ├── trans-title (34px, 白色)
            └── trans-row ×2
                ├── trans-advantage (绿色, 含勾号SVG + "优势：" + 文字)
                └── trans-needfix (橙色, 含警告SVG + "需补齐：" + 文字)
```

#### 2.5.2 卡片规格
```css
trans-card:
  display:flex; align-items:center; gap:30px
  padding:40px 50px; border-radius:24px
  background:rgba(30,41,59,0.5)
  border:1px solid rgba(255,255,255,0.06)
  backdrop-filter:blur(20px)

trans-icon-box:
  80×80px; border-radius:20px
  SVG: 40×40px; stroke-width:2; fill:none

trans-advantage:
  color:#22C55E(绿)
  内含SVG勾号: 24×24px, stroke-width:2.5
  格式: [勾号SVG] "优势：" + 描述文字

trans-needfix:
  color:#F59E0B(橙)
  内含SVG警告: 24×24px, stroke-width:2.5
  格式: [警告SVG] "需补齐：" + 描述文字
```

#### 2.5.3 SVG图标代码
- 优势勾号: `<polyline points="20 6 9 17 4 12"/>`
- 警告三角: `<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>`
- 卡图标1(开发→代码): 同场景1 c1
- 卡图标2(运维→服务器): `<rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/>`
- 卡图标3(售前→显示器): `<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>`

#### 2.5.4 动画时间线
| 时间 | 元素 | 动画 | 参数 |
|------|------|------|------|
| 40.59s | scene5 | 淡入 | fromTo opacity:0→1, duration:0.2 |
| 40.59s | pill-badge | 下滑入 | y:-30→0, opacity:0→1, duration:0.4 |
| 40.76s | main-title | 上滑入 | y:30→0, opacity:0→1, duration:0.4 |
| 40.85s | trans-card ×3 | 左侧stagger滑入 | x:-60→0, opacity:0→1, stagger:0.25, duration:0.5, ease:power2.out |
| 41.29s | bottom-card | 上滑入 | y:100→0, opacity:0→1, duration:0.5 |
| 50.80s | scene5 | 淡出 | opacity:1→0, duration:0.3, ease:power2.in |
| 51.10s | scene5 | set hidden | visibility:hidden |

#### 2.5.5 文案模式
```
pill-badge: 英文标签（如 "Career Shift"）
main-title: "哪类人转型最容易成功？"
trans-card ×3:
  - 来源(如"从开发(Dev)转型") + 图标
  - 优势: 一句话描述已有能力
  - 需补齐: 一句话描述待提升能力
bottom-card: 总结转型路径（约40字）
TTS: 与bottom-card相同
```

---

### 场景6：价值宣言收尾 (51.10 - 62.47s)

#### 2.6.1 布局结构
```
content-area (justify-content:center)
├── brand-label (32px, 700, 青蓝色#22D3EE, letter-spacing:8px, 居中)
├── main-quote (52px, 700, line-height:1.8, max-width:2000px, 居中)
│   ├── quote-line1 (白色)
│   ├── quote-line2 (青绿#00D4AA)
│   └── quote-line3 (青绿#00D4AA)
├── divider (80×3px, rgba(255,255,255,0.2), 居中, margin:40px auto)
└── sub-quote (36px, 400, 灰色#94A3B8, 居中)
```

#### 2.6.2 规格细节
```css
brand-label:
  color:#22D3EE; font-size:32px; font-weight:700
  letter-spacing:8px; margin-bottom:60px; text-align:center

main-quote:
  font-size:52px; font-weight:700; line-height:1.8
  text-align:center; max-width:2000px; margin:0 auto

quote-line1: color:#FFFFFF (白色, 引入句)
quote-line2: color:#00D4AA (青绿, 核心句)
quote-line3: color:#00D4AA (青绿, 核心句)

divider:
  width:80px; height:3px
  background:rgba(255,255,255,0.2)
  margin:40px auto; border-radius:2px

sub-quote:
  font-size:36px; color:#94A3B8
  text-align:center; font-weight:400
```

#### 2.6.3 动画时间线
| 时间 | 元素 | 动画 | 参数 |
|------|------|------|------|
| 51.10s | scene6 | 淡入 | fromTo opacity:0→1, duration:0.2 |
| 51.10s | brand-label | 下滑入 | y:-20→0, opacity:0→1, duration:0.5 |
| 51.27s | quote-line1 | 上滑入 | y:30→0, opacity:0→1, duration:0.5 |
| 51.44s | quote-line2 | 上滑入 | y:30→0, opacity:0→1, duration:0.5 |
| 51.61s | quote-line3 | 上滑入 | y:30→0, opacity:0→1, duration:0.5 |
| 51.80s | divider | 展开淡入 | width:0→80px, opacity:0→1, duration:0.4 |
| 51.88s | sub-quote | 上滑入 | y:20→0, opacity:0→1, duration:0.4 |
| 51.97s | bottom-card | 上滑入 | y:100→0, opacity:0→1, duration:0.5 |

#### 2.6.4 文案模式
```
brand-label: 英文品牌词（如 "TECH · IMPACT"）
main-quote: 3行金句
  line1(白): 引入否定句 "XX绝不是..."
  line2(青绿): 核心定义 "它是为那些..."
  line3(青绿): 延续 "想去...的人准备的"
divider: 分隔线
sub-quote: 一句话精华（如 "把代码，变成真金白银的交付"）
bottom-card: 总结+IP署名（如 "记住...我是XX，XX共生，利人利己"）
TTS: 与bottom-card相同
```

---

## 三、动画效果汇总

### 3.1 6种动画风格分配

| 风格 | 使用场景 | GSAP代码模板 |
|------|---------|-------------|
| 缩放弹入 | 场景1 icon-cell | `from(scale:0, opacity:0, ease:'back.out(1.7)')` |
| 左右滑入 | 场景2 stereo-card, 场景4 trait-card | `from(x:±80, opacity:0, ease:'power2.out')` |
| 旋转弹入 | 场景3 skill-icon-box | `from(rotation:-15, scale:0.8, opacity:0, ease:'back.out(1.7)')` |
| 进度条填充 | 场景3 skill-fill | `to(width:'XX%', ease:'power2.out')` |
| stagger逐项 | 场景4 trait-item, 场景5 trans-card | `from(y:30, opacity:0, stagger:0.1~0.25)` |
| 逐行打字机 | 场景6 quote-line | `from(y:30, opacity:0, stagger:0.17)` |
| 发光脉冲 | 场景2 center card | `to(boxShadow:'0 0 60px ...', yoyo:true, repeat:1)` |
| 分割线展开 | 场景6 divider | `from(width:0, opacity:0)` |

### 3.2 通用入场动画

每个场景的 pill-badge 和 main-title 都使用相同模式：
```
pill-badge: from(y:-30, opacity:0, duration:0.4)  → 场景起始时间
main-title: from(y:30, opacity:0, duration:0.4)   → 场景起始+0.17s
bottom-card: from(y:100, opacity:0, duration:0.5) → 场景起始+0.5~0.9s
```

### 3.3 场景过渡规则

```
场景N结束前0.3s: master.to('#sceneN', {opacity:0, duration:0.3, ease:'power2.in'}, endN-0.3)
场景N结束: master.set('#sceneN', {visibility:'hidden'}, endN)
场景N+1开始: master.set('#sceneN+1', {visibility:'visible'}, endN)
场景N+1淡入: master.fromTo('#sceneN+1', {opacity:0}, {opacity:1, duration:0.2}, endN)
```

---

## 四、字幕系统规格

### 4.1 字幕数据结构
```javascript
const SUBTITLES = [
  {scene: N, start: X.X, end: Y.Y, text: "字幕文本"}
];
```

### 4.2 字幕拆分规则
1. 每条字幕不超过15个中文字符
2. 按TTS文本的标点（逗号/句号/问号）断句
3. start时间 = 该句TTS音频的起始时间
4. end时间 = 该句TTS音频的结束时间
5. 每个场景约3-5条字幕

### 4.3 字幕更新机制
```javascript
window.updateSubtitle = function(time) {
  // 遍历SUBTITLES找到当前时间的字幕
  // 隐藏所有.subtitle-bar
  // 显示匹配的字幕条并设置文本
};
// seekTo中自动调用updateSubtitle
```

---

## 五、时间线计算规则

### 5.1 从TTS到视频时间线

```
1. 生成6段TTS音频 (scene1.mp3 ~ scene6.mp3)
2. 用ffprobe测量每段时长 D1~D6
3. 计算场景时间线:
   场景1: start=0, tts_start=0, tts_end=D1, scene_end=D1+0.5(尾部留白)
   场景2: start=scene1_end, tts_start=scene1_end+0.5(间隔), tts_end=tts_start+D2, scene_end=tts_end
   场景N: start=scene(N-1)_end, tts_start=start+0.5, tts_end=tts_start+DN, scene_end=tts_end
4. TOTAL_DURATION = scene6_end
5. TOTAL_FRAMES = round(TOTAL_DURATION * 25)
6. 淡出时间点 = sceneN_end - 0.3
7. 隐藏时间点 = sceneN_end
```

### 5.2 音频混合

```
1. 每段TTS的延迟 = 该段tts_start * 1000 (毫秒)
2. FFmpeg命令:
   ffmpeg -i scene1.mp3 -i scene2.mp3 ... -i scene6.mp3
     -filter_complex "[0:a]adelay=D1|D1[a1]; [1:a]adelay=D2|D2[a2]; ...
                      [a1][a2]...[a6]amix=inputs=6:normalize=0[v]"
     -volume 1.8 -ar 48000 -ac 1 final_audio.wav
3. 如需调速: atempo=1.15 (加速15%), 同时所有GSAP时间戳 × (1/1.15)
```

### 5.3 字幕时间码
```
字幕start = TTS对应句子的实际起始时间
字幕end = TTS对应句子的实际结束时间
计算方法: 按文本长度等比例分配该场景TTS总时长
  句子时长 = (句字数 / 场景TTS总字数) * 场景TTS时长
```

---

## 六、SVG图标库

### 6.1 概念图标 (场景1用)

| 概念维度 | SVG代码 | 颜色 |
|---------|---------|------|
| 技术/代码 | `<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>` | #00D4AA |
| 人物/协作 | `<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>` | #22C55E |
| 业务/公文包 | `<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><line x1="3" y1="13" x2="21" y2="13"/>` | #F59E0B |
| 创新/网络 | `<circle cx="12" cy="12" r="3"/><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>` + 4条连线 | #A855F7 |

### 6.2 状态图标

| 状态 | SVG代码 | 颜色 |
|------|---------|------|
| 正确/勾号 | `<polyline points="20 6 9 17 4 12"/>` | #00D4AA / #22C55E |
| 错误/叉号 | `<line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/>` | #FF6B6B |
| 警告 | `<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>` | #F59E0B |
| 禁止 | `<circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>` | #FF6B6B |

### 6.3 功能图标

| 功能 | SVG代码 |
|------|---------|
| 对话/沟通 | `<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>` |
| 柱状图/数据 | `<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>` |
| 服务器/运维 | `<rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/>` |
| 显示器/售前 | `<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>` |
| 扳手/修复 | `<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>` |
| 盾牌/抗压 | `<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>` |
| 飞机/出差 | `<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5-.3.5-.2 1.1.3 1.6L9 12l-4 4-3-.5L1 17l3 1 1 3 1.5-1L6 17l4-4 3.7 4.9c.5.5 1.1.6 1.6.3.4-.2.6-.6.5-1z"/>` |
| 时钟/作息 | `<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>` |

### 6.4 SVG通用规则
```css
所有SVG: viewBox="0 0 24 24" stroke="currentColor" fill="none"
线条属性: stroke-linecap="round" stroke-linejoin="round"
粗细范围: stroke-width 1.8 ~ 2.5
图标尺寸: 根据容器，24px/32px/36px/40px/72px
```

---

## 七、新主题适配清单

给定一个新的AI概念主题，按以下清单逐项填充：

### 7.1 需要提供的文案

| 序号 | 内容 | 字数 | 示例 |
|------|------|------|------|
| 1 | 右上角标签 | - | "AI产品概念扫盲 \| 第4课 ★ 深度解析" |
| 2 | 场景1标题 | 问句 | "什么是RAG?" |
| 3 | 场景1副标题 | 8-12字 | "检索与生成的完美结合" |
| 4 | 场景1标签 | 4-6字 | "技术原理剖析" |
| 5 | 场景1标签描述 | 10-15字 | "拒绝雾里看花，搞懂检索增强" |
| 6 | 场景1底部金句 | 30-50字 | 引入性文案 |
| 7 | 场景2标签 | 英文 | "STEREOTYPE VS REALITY" |
| 8 | 场景2标题 | - | "关于RAG的两大误解" |
| 9 | 场景2左卡片 | 标题+3条 | 偏见一 |
| 10 | 场景2中卡片 | 标题+副标题+2条 | 真相 |
| 11 | 场景2右卡片 | 标题+3条 | 偏见二 |
| 12 | 场景2底部金句 | 40字 | 真相总结 |
| 13 | 场景3标签 | 英文 | "The R-A-G Model" |
| 14 | 场景3标题 | - | "RAG三步核心流程" |
| 15 | 场景3技能条×3 | 名+百分比+描述 | 3个核心步骤 |
| 16 | 场景3底部金句 | 50字 | 模型总结 |
| 17 | 场景4标签 | 英文 | "Use Case Checklist" |
| 18 | 场景4标题 | - | "哪些场景适合用RAG？" |
| 19 | 场景4左卡片 | 标题+3项(标题+描述) | 适合场景 |
| 20 | 场景4右卡片 | 标题+3项(标题+描述) | 不适合场景 |
| 21 | 场景4底部金句 | 40字 | 适合/不适合总结 |
| 22 | 场景5标签 | 英文 | "Implementation Path" |
| 23 | 场景5标题 | - | "如何上手RAG？" |
| 24 | 场景5卡片×3 | 来源+优势+需补齐 | 3条实践路径 |
| 25 | 场景5底部金句 | 40字 | 路径总结 |
| 26 | 场景6品牌词 | 英文 | "RETRIEVAL · GENERATION" |
| 27 | 场景6金句 | 3行 | 价值宣言 |
| 28 | 场景6副标语 | 10-15字 | 精华提炼 |
| 29 | 场景6底部金句 | 40-60字 | 总结+IP署名 |
| 30 | 6段TTS文本 | 每段30-60字 | 与底部金句一致 |

### 7.2 需要选择的图标

| 场景 | 需选图标数 | 选择依据 |
|------|-----------|---------|
| 场景1 | 4个概念图标 | 代表主题的4个维度 |
| 场景2 | 2个叉号图标 | 左右偏见各1个 |
| 场景3 | 3个功能图标 | 对应3个核心步骤 |
| 场景4 | 2个大图标(勾/叉) + 6个小图标 | 适合/不适合各1大3小 |
| 场景5 | 3个来源图标 + 6个状态图标(3勾+3警告) | 每条路径1来源+1优势+1需补齐 |
| 场景6 | 无图标 | 纯文字场景 |

### 7.3 时间线参数表（待填）

| 场景 | TTS时长 | 场景start | tts_start | tts_end | scene_end | 淡出点 |
|------|---------|-----------|-----------|---------|-----------|--------|
| 1 | D1=___ | 0 | 0 | D1 | D1+0.5 | D1+0.2 |
| 2 | D2=___ | S1_end | S1_end+0.5 | tts_start+D2 | tts_end | scene_end-0.3 |
| 3 | D3=___ | S2_end | S2_end+0.5 | tts_start+D3 | tts_end | scene_end-0.3 |
| 4 | D4=___ | S3_end | S3_end+0.5 | tts_start+D4 | tts_end | scene_end-0.3 |
| 5 | D5=___ | S4_end | S4_end+0.5 | tts_start+D5 | tts_end | scene_end-0.3 |
| 6 | D6=___ | S5_end | S5_end+0.5 | tts_start+D6 | tts_end | scene_end-0.3 |

TOTAL_DURATION = S6_end
TOTAL_FRAMES = round(TOTAL_DURATION × 25)

---

## 八、渲染参数

### 8.1 Playwright渲染
```python
viewport = {"width": 2400, "height": 3200}
screenshot: type="jpeg", quality=95, full_page=False
每帧间隔: time.sleep(0.03)
断点续传: 检查frames_dir中已有帧数
```

### 8.2 FFmpeg编码
```
ffmpeg -framerate 25 -i frame_%06d.jpg -i final_audio.wav \
  -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -profile:v high -level 5.1 \
  -c:a aac -b:a 192k -ar 48000 -ac 1 \
  -shortest -movflags +faststart output.mp4
```

### 8.3 edge-tts参数
```
voice: zh-CN-YunjianNeural
rate: -10%
命令: edge-tts --voice zh-CN-YunjianNeural --rate=-10% --text "文本" --write-media scene.mp3
```
