import os
import sounddevice as sd
import soundfile as sf
import pandas as pd
import numpy as np

# ======= 配置项 ========
DATA_DIR = r"F:\Program\TTS\my_dataset"
CSV_PATH = os.path.join(DATA_DIR, "metadata.csv")
WAV_DIR = os.path.join(DATA_DIR, "wavs")
SAMPLERATE = 22050
CHANNELS = 1
DURATION = 5  # 默认录音 5 秒，可手动停止
# ======================

os.makedirs(WAV_DIR, exist_ok=True)
df = pd.read_csv(CSV_PATH, sep="|", header=None, names=["filename", "text"])

print(f"共需录制 {len(df)} 条语音。准备开始！\n")

for idx, row in df.iterrows():
    filename, text = row["filename"], row["text"]
    output_path = os.path.join(WAV_DIR, f"{filename}.wav")
    
    print(f"🎤 第 {idx + 1}/{len(df)} 条：{text}")
    input("👉 按 Enter 开始录音...")

    print("🔴 正在录音，请朗读...")
    recording = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=CHANNELS, dtype='int16')
    sd.wait()
    print("✅ 录音完成！")

    # 保存为 PCM 16-bit WAV 文件
    sf.write(output_path, recording, SAMPLERATE, subtype='PCM_16')
    print(f"💾 已保存：{output_path}\n")

print("✅ 所有录音完成！")
