# Scam Audio Detection App

This project is a Streamlit-based web application that detects whether an audio message is a scam. It integrates two main machine learning pipelines:

1. **Audio-to-Text (ASR)** – converts uploaded audio into text  
2. **Text Classification** – predicts whether the message is a scam  

---

## Features

- Upload audio files (FLAC format)
- Automatic speech recognition (ASR)
- Scam detection using a fine-tuned Hugging Face model
- User-friendly interface with risk warnings and safety advice

---

## Pipeline Overview

### Pipeline 1: Audio → Text
- Model: `openai/whisper-tiny`
- Converts uploaded audio into transcribed text

### Pipeline 2: Text → Scam Detection
- Model: `MrTher/scam_detector`
- Classifies text as:
  - **Scam**
  - **Not Scam**

---

## Demo

You can try the deployed app here:  
👉 *(Paste your Streamlit link here)*
