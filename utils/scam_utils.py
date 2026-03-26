import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

HF_MODEL = "MrTher/scam_detector"
LOCAL_MODEL = "./local_models/scam_detector"

tokenizer = None
model = None

def load_model():
    global tokenizer, model

    if tokenizer is not None and model is not None:
        return

    try:
        print("Loading model from Hugging Face...")
        tokenizer = AutoTokenizer.from_pretrained(HF_MODEL)
        model = AutoModelForSequenceClassification.from_pretrained(HF_MODEL)
        print("Loaded from Hugging Face")

    except Exception as e:
        print("HF failed, loading local model:", e)

        tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL)
        model = AutoModelForSequenceClassification.from_pretrained(LOCAL_MODEL)

def predict_scam(text):
    load_model()

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    pred_id = torch.argmax(outputs.logits, dim=1).item()

    label_map = {
        0: "Not Scam",
        1: "Scam"
    }

    return label_map.get(pred_id, f"LABEL_{pred_id}")
