# AI产品概念扫盲视频 · 制作方法（Codex 版）

把任意 AI 概念做成一条竖版科普动画视频。核心思路一句话：**先写 6 幕脚本 → 用 HTML/CSS/GSAP 做一个会动的"网页舞台" → edge-tts 配音 → 按音频时长倒推动画时间线 → Playwright 逐帧截图 → FFmpeg 把图和声音压成 mp4**。

用户说"做一期 XX 的扫盲视频 / XX 概念科普视频"时，走下面完整流程。

## 输出规格（固定）

| 项目 | 值 |
|------|-----|
| 分辨率 | 2400×3200（3:4 竖版） |
| FPS | 25 |
| 时长 | 60~90 秒 |
| 音频 | AAC 192k / 48kHz / mono |
| 语音 | edge-tts `zh-CN-YunjianNeural`，`rate=-10%` |
| 风格 | 深色科技风 + 玻璃拟态卡片 + SVG 线条图标（禁止 emoji） |

## 参考文件（做视频前必读）

- `references/video_spec.md` — **最重要**。逐像素拆解 6 个场景的布局、动画时间线、图标代码、文案模式、新主题适配清单（30 项）
- `references/full_script.json` — 脚本 JSON 结构示例
- `references/video_template.html` — 完整 HTML/CSS/GSAP 模板（直接改这个，别从零写）
- `references/render_video.py` — 参数化渲染脚本（改顶部配置区即可跑）

## 完整工作流（9 步）

### 第 1 步：选题查重
- 读 `output/done-list.txt`（没有就新建），确认主题没做过
- 已做过的主题参考（已到第 18 课）：MCP、AI Agent、RAG、Fine-tuning、Embedding、RLHF、Multimodal、MoE、Diffusion、思维链、知识图谱、向量数据库、推理模型、模型蒸馏、Function Calling、Deep Search、世界模型、数字孪生
- 在工作目录建 `output/YYYYMMDD_主题名/`，本视频所有产物都放这里

### 第 2 步：写脚本（6 幕固定结构）
按 `references/video_spec.md` 第七节"新主题适配清单"逐项生成 30 项文案：

| 场景 | 作用 | 核心内容 |
|------|------|---------|
| 1 概念引入 | 抛问题+常见误解 | 4 图标矩阵、问句标题、渐变副标题、30-50字引入金句 |
| 2 误解 vs 真相 | 破除刻板印象 | 左右两张偏见卡（各3条）+ 中间高亮真相卡 |
| 3 原理模型 | 讲清楚怎么运作 | 3 条技能条/流程条（名称+百分比+描述） |
| 4 适用诊断 | 谁适合/不适合 | 左绿卡（适合×3）+ 右红卡（不适合×3） |
| 5 上手路径 | 怎么实践 | 3 张卡：来源→优势（绿）+ 需补齐（橙） |
| 6 价值收尾 | 金句升华 | 品牌词 + 3 行大金句 + 副标语 + IP 署名 |

- 每幕都含：标题、英文标签、正文、底部白卡金句、TTS 文本（TTS = 底部金句内容）
- 存成 `script.json`，结构参考 `references/full_script.json`
- **脚本先给用户确认，再往下做**（允许迭代修改）

### 第 3 步：做 HTML + GSAP 动画
- 复制 `references/video_template.html` 到工作目录，替换文案和图标
- 设计规范速查：
  - 背景：`radial-gradient(ellipse at 50% 40%, #0F172A 0%, #050810 80%)`
  - 主色 `#00D4AA`（青绿）；辅色 `#3B82F6` `#A855F7` `#F59E0B` `#22C55E` `#FF6B6B`
  - 玻璃卡：`rgba(30,41,59,0.6)` + `backdrop-filter:blur(20px)` + 1px 白色低透明边框
  - 底部白卡：满宽、圆角 `32px 32px 0 0`、最小高 480px、深灰字 `#1F2937`
  - 字幕条：`bottom:500px` 居中、黑底半透明+模糊、36px 白字
  - 进度条：顶部 6px，`linear-gradient(90deg, #00D4AA, #F59E0B)`
  - 图标：SVG `viewBox="0 0 24 24"`、`stroke-width:1.8~2.5`、`fill:none`
- GSAP 关键写法（**这些是硬约束，违反会翻车**）：
  - 单一 master timeline：`gsap.timeline({ paused: true })`
  - **场景可见性必须用 `master.set()`，绝不能用 `add()` 回调** —— 渲染靠 `seek()` 跳时间点，`seek()` 不触发 `add()` 回调，用了会黑屏
  - 每个场景结束前 0.3s 淡出，下一场景 0.2s 淡入
  - 6 个场景至少用 4 种不同动画（缩放弹入 / 滑入 / 进度条填充 / stagger 逐项 / 打字机逐行 / 旋转弹入），别全用同一种
  - 暴露渲染接口：
    ```javascript
    window.FDE_VIDEO = {
      totalDuration: TOTAL_DURATION,
      fps: 25,
      seekTo: function(time) {
        master.seek(time);
        if (window.updateSubtitle) window.updateSubtitle(time);
      }
    };
    ```

### 第 4 步：TTS 配音
- 每幕一段，共 6 个 mp3：
  ```bash
  edge-tts --voice zh-CN-YunjianNeural --rate=-10% --text "该幕TTS文本" --write-media scene1.mp3
  ```
- 用 ffprobe 测每段实际时长 D1~D6（**别估算，必须实测**）

### 第 5 步：算时间线 + 混音
时间线公式（由音频时长倒推动画）：
```
场景1: start=0, tts_start=0, scene_end=D1+0.5
场景N: start=上一幕end, tts_start=start+0.5(幕间留白), scene_end=tts_start+DN
TOTAL_DURATION = 场景6的end
TOTAL_FRAMES = round(TOTAL_DURATION × 25)
```
把算好的时间戳填进 HTML 的 GSAP 时间线（**场景出现时间 = 配音时间 - 0.5s，留呼吸感**）。

混音（6 段按各自 tts_start 延迟后叠成一条）：
```bash
ffmpeg -i scene1.mp3 -i scene2.mp3 ... -i scene6.mp3 \
  -filter_complex "[0:a]adelay=D1|D1[a1];...;[a1]...[a6]amix=inputs=6:normalize=0" \
  -volume 1.8 -ar 48000 -ac 1 final_audio.wav
```
（adelay 的参数是毫秒 = tts_start × 1000）

### 第 6 步：字幕
- 按标点把每幕 TTS 文本断句，**每条 ≤15 个中文字**
- 时间码按字数比例分：`句子时长 = (句字数 / 该幕总字数) × 该幕TTS时长`
- 数据塞进 HTML 的 `SUBTITLES` 数组：`{scene, start, end, text}`
- `window.updateSubtitle(time)` 在 seekTo 时自动切换字幕条

### 第 7 步：逐帧渲染 + 合成
- 改 `references/render_video.py` 顶部配置区（HTML 路径、帧目录、音频、总时长），然后 `python render_video.py`
- 脚本逻辑：Playwright 无头浏览器 2400×3200 → 每帧 `FDE_VIDEO.seekTo(帧号/25)` → sleep 0.03s → 截 JPEG quality 95
- **支持断点续传**：中断后重跑会从已有帧继续
- 渲染完自动调 FFmpeg 合成：
  ```
  libx264 / preset medium / crf 20 / yuv420p / profile high level 5.1
  aac 192k / 48kHz / mono / -shortest -movflags +faststart
  ```

### 第 8 步：封面 + 小红书文案
- 封面 `cover.jpg`：1200×1600，PIL 画——深色径向渐变背景 + 轨道环装饰 + 大标题 + 集数 + 概念英文词 + IP 署名（字体用 `C:\Windows\Fonts\msyhbd.ttc`）
- 文案 `post.txt`：小红书正文 ≤100 字 + 5~8 个话题标签（#AI扫盲 #概念科普 等）

### 第 9 步：登记
往 `output/done-list.txt` 追加一行：
```
YYYYMMDD | 第N课 | 主题中文 | 主题英文全称 | 文件名.mp4
```

## 必须记住的坑（前辈踩过的）

1. **GSAP 用 `set()` 不用 `add()`** —— seek 渲染的黑屏坑
2. **场景起始 = TTS 起始 - 0.5s** —— 音画同步公式
3. **TTS 时长必须实测**（ffprobe），估算必翻车
4. **TOTAL_DURATION 要和 HTML 里的一致**，渲染脚本和进度条都依赖它
5. 渲染前自检：每个场景的 `set(visible)` 时间点、字幕 start/end、进度条总时长，三者是否都对齐了音频
6. 渲染中断别慌，直接重跑脚本会续传
7. 想调速：用 `atempo=1.15` 加速音频，同时 GSAP 所有时间戳 × (1/1.15)

## 环境准备（首次使用）

```bash
pip install playwright edge-tts pillow
playwright install chromium
# ffmpeg：系统装一个（winget install ffmpeg 或官网下载），渲染脚本会自动从 PATH 找
```

## 目录结构约定

```
codex-video-method/
├── AGENTS.md              ← 本文件
├── references/            ← 模板和规格（只读参考，别改）
│   ├── video_spec.md
│   ├── video_template.html
│   ├── render_video.py
│   └── full_script.json
└── output/
    ├── done-list.txt      ← 已做主题登记
    └── YYYYMMDD_主题/
        ├── script.json        ← 6幕脚本
        ├── video_template.html← 本期改好的动画页
        ├── scene1~6.mp3       ← 分幕配音
        ├── final_audio.wav     ← 混音后音轨
        ├── render_frames/      ← 逐帧截图（可删）
        ├── 概念名.mp4          ← 成片
        ├── cover.jpg           ← 封面
        └── post.txt            ← 小红书文案
```
