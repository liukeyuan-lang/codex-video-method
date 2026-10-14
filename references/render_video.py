"""
视频逐帧渲染脚本 - AI产品概念扫盲
用法: 修改下方 === 配置区 === 的变量，然后运行 python render_video.py
支持断点续传：如中断后重新运行，会从已有帧继续
"""
from playwright.sync_api import sync_playwright
import os
import shutil
import time
import subprocess
import sys

# === 配置区（每次使用时修改这里） ===
# HTML模板路径
html_path = r"./video_template.html"
# 帧输出目录
frames_dir = r"./render_frames"
# 音频文件路径
audio_path = r"./final_audio.wav"
# 最终视频输出路径
output_video = r"./output.mp4"
# 视频总时长（秒）- 必须与HTML中的TOTAL_DURATION一致
TOTAL_DURATION = 62.47
# === 配置区结束 ===

# FFmpeg路径：从系统PATH查找，需提前安装（如 winget install ffmpeg）
FFMPEG = shutil.which("ffmpeg")

FPS = 25
TOTAL_FRAMES = round(TOTAL_DURATION * FPS)

os.makedirs(frames_dir, exist_ok=True)

print(f"=== 帧渲染流水线 ===")
print(f"HTML模板: {html_path}")
print(f"音频文件: {audio_path}")
print(f"输出视频: {output_video}")
print(f"总帧数: {TOTAL_FRAMES}")
print(f"分辨率: 2400x3200")
print(f"FPS: {FPS}")
print(f"时长: {TOTAL_DURATION}s")
print()

# 检查HTML和音频文件是否存在
if not FFMPEG:
    print("错误: 未找到 ffmpeg，请先安装（如 winget install ffmpeg）后重试")
    sys.exit(1)
if not os.path.exists(html_path):
    print(f"错误: HTML文件不存在: {html_path}")
    sys.exit(1)
if not os.path.exists(audio_path):
    print(f"错误: 音频文件不存在: {audio_path}")
    sys.exit(1)

# 检查已有帧以支持断点续传
existing_frames = [f for f in os.listdir(frames_dir) if f.startswith("frame_") and f.endswith(".jpg")]
start_frame = len(existing_frames)
print(f"已有帧: {start_frame}/{TOTAL_FRAMES}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 2400, "height": 3200})
    
    # 加载HTML
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    time.sleep(3)
    
    # 验证GSAP和字幕系统已加载
    gsap_ok = page.evaluate("typeof gsap !== 'undefined' && typeof window.FDE_VIDEO !== 'undefined'")
    if not gsap_ok:
        print("错误: GSAP 或 FDE_VIDEO 未加载!")
        browser.close()
        sys.exit(1)
    
    # 验证字幕系统
    subtitle_ok = page.evaluate("typeof window.updateSubtitle === 'function'")
    if subtitle_ok:
        print("字幕系统已加载")
    else:
        print("警告: 字幕系统未检测到（updateSubtitle函数不存在）")
    
    print("GSAP已加载，开始帧捕获...\n")
    render_start = time.time()
    
    for frame_num in range(start_frame, TOTAL_FRAMES):
        time_sec = frame_num / FPS
        
        # Seek到目标时间（同时更新字幕）
        page.evaluate(f"window.FDE_VIDEO.seekTo({time_sec})")
        
        # 等待DOM更新
        time.sleep(0.03)
        
        # 截图
        frame_path = os.path.join(frames_dir, f"frame_{frame_num:06d}.jpg")
        page.screenshot(path=frame_path, type="jpeg", quality=95, full_page=False)
        
        # 进度报告
        if frame_num % 50 == 0 or frame_num == TOTAL_FRAMES - 1:
            elapsed = time.time() - render_start
            pct = (frame_num + 1) / TOTAL_FRAMES * 100
            eta = elapsed / max(frame_num - start_frame + 1, 1) * (TOTAL_FRAMES - frame_num - 1)
            print(f"  帧 {frame_num+1}/{TOTAL_FRAMES} ({pct:.1f}%) - t={time_sec:.2f}s - ETA: {eta:.0f}s")
        
        # 保存断点
        if frame_num % 100 == 0 and frame_num > 0:
            with open(os.path.join(frames_dir, "resume.txt"), "w") as f:
                f.write(str(frame_num + 1))
    
    browser.close()

print(f"\n=== 全部 {TOTAL_FRAMES} 帧渲染完成! ===")

# FFmpeg合成视频
print("\n=== 使用FFmpeg合成视频 ===")

result = subprocess.run([
    FFMPEG, "-y",
    "-framerate", str(FPS),
    "-i", os.path.join(frames_dir, "frame_%06d.jpg"),
    "-i", audio_path,
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "20",
    "-pix_fmt", "yuv420p",
    "-profile:v", "high",
    "-level", "5.1",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-ac", "1",
    "-shortest",
    "-movflags", "+faststart",
    output_video
], capture_output=True, text=True)

if os.path.exists(output_video):
    size_mb = os.path.getsize(output_video) / 1024 / 1024
    print(f"\n=== 视频创建成功! ===")
    print(f"输出: {output_video}")
    print(f"大小: {size_mb:.1f} MB")
    print(f"分辨率: 2400x3200")
    print(f"FPS: {FPS}")
    print(f"时长: ~{TOTAL_DURATION}s")
else:
    print(f"\n视频创建失败!")
    print(f"错误: {result.stderr[-1000:]}")
