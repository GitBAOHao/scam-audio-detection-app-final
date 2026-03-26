from huggingface_hub import snapshot_download

repo_id = "MrTher/scam_detector"

local_dir = "./local_models/scam_detector"

snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    local_dir_use_symlinks=False
)

print("Model downloaded successfully!")
