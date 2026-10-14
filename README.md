# AI 产品概念扫盲视频 · 制作方法（Codex 版）

一套"把任意 AI 概念做成竖版科普动画视频"的完整工作流。原方法来自 TRAE 技能实战打磨（已量产 18 期），本仓库把它整理成 Codex（或任何 AI 编程工具）可直接复用的形式。

## 成品长什么样

- 竖版 3:4（2400×3200），60~90 秒
- 深色科技风 + 玻璃拟态卡片 + SVG 线条图标
- 固定 6 幕结构：抛问题 → 破误解 → 讲原理 → 谁适合 → 怎么上手 → 金句收尾
- 每期自动产出：成片 mp4 + 封面图 + 小红书文案

## 原理一句话

不录屏、不剪辑——**做一个会动的"网页舞台"（HTML/CSS/GSAP），用 edge-tts 配音，按音频时长倒推动画时间线，Playwright 逐帧截图，FFmpeg 把图和声音压成 mp4**。

```
脚本(6幕) → HTML动画页 → TTS配音 → 实测时长倒推时间线 → 混音
        → 字幕对齐 → 逐帧截图(25fps) → FFmpeg合成 → 封面+文案
```

## 快速开始

1. 用 Codex 打开本文件夹（它会自动读取 `AGENTS.md`）
2. 说一句："做一期 XX 的扫盲视频"（XX = 任意 AI 概念，如 RAG、MoE）
3. 全流程自动跑完，产物在 `output/日期_主题/`

首次使用先装依赖：

```bash
pip install playwright edge-tts pillow
playwright install chromium
winget install ffmpeg   # 或官网下载
```

## 文件说明

| 文件 | 用途 |
|------|------|
| `AGENTS.md` | 完整工作流指令（Codex 自动读取，9 步全流程 + 踩坑清单） |
| `references/video_spec.md` | 逐像素规格拆解：6 个场景的布局、动画、图标、文案模式 |
| `references/video_template.html` | HTML/CSS/GSAP 完整模板（直接改，别从零写） |
| `references/render_video.py` | 逐帧渲染脚本（支持断点续传） |
| `references/full_script.json` | 6 幕脚本 JSON 结构示例 |

## 核心经验（前辈踩坑总结）

1. **GSAP 必须用 `set()` 控制场景可见性，不能用 `add()` 回调**——渲染靠 `seek()` 跳时间点，`seek()` 不触发回调，用错会整片黑屏
2. **音画同步公式：场景出现时间 = 配音开始时间 − 0.5s**
3. **TTS 时长必须 ffprobe 实测**，估算必翻车
4. 渲染中断直接重跑脚本，支持断点续传
