import os

# 音频文件夹路径
wav_dir = r"F:\Program\TTS\my_dataset\wavs"

# 遍历文件夹中所有文件
for filename in os.listdir(wav_dir):
    if filename.endswith(".wav"):
        # 去掉扩展名获取纯数字名
        name = os.path.splitext(filename)[0]
        try:
            # 仅处理数字文件名
            new_name = f"{int(name):04d}.wav"
            src = os.path.join(wav_dir, filename)
            dst = os.path.join(wav_dir, new_name)
            os.rename(src, dst)
            print(f"✅ 重命名: {filename} -> {new_name}")
        except ValueError:
            print(f"⚠️ 跳过非数字文件名: {filename}")
