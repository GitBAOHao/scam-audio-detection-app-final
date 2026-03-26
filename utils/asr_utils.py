from transformers import pipeline
import tempfile

transcriber = None

def load_asr_model():
    global transcriber
    if transcriber is None:
        transcriber = pipeline(
            "automatic-speech-recognition",
            model="distil-whisper/distil-large-v3"
        )

def transcribe_audio(uploaded_file):
    load_asr_model()

    # 把上传文件暂存成一个临时 flac 文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=".flac") as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    output_text = transcriber(temp_audio_path)
    content = output_text["text"]

    return content