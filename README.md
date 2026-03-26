# Scam Audio Detection App

This app detects scam messages from audio input.

Pipeline:
1. Audio → Text (ASR using Whisper)
2. Text → Scam Detection (fine-tuned model)

Model:
- Hugging Face: MrTher/scam_detector

Usage:
- Upload a FLAC audio file
- The app will transcribe and classify it