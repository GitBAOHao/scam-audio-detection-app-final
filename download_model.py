from huggingface_hub import snapshot_download

# 模型名（你的）
repo_id = "MrTher/scam_detector"

# 本地保存路径
local_dir = "./local_models/scam_detector"

snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    local_dir_use_symlinks=False
)

print("Model downloaded successfully!")