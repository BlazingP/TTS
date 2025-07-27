# check_cuda.py
import torch

print("🚀 CUDA 是否可用:", torch.cuda.is_available())
print("🎯 使用的设备数量:", torch.cuda.device_count())
print("🧠 当前设备:", torch.cuda.current_device())
print("💻 当前 GPU 名称:", torch.cuda.get_device_name(0))
print("🧮 CUDA 版本:", torch.version.cuda)
