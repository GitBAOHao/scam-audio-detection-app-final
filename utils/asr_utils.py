from transformers import pipeline
import tempfile

transcriber = None

def load_asr_model():
    global transcriber
    if transcriber is None:
        transcriber = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny"
        )

def transcribe_audio(uploaded_file):
    load_asr_model()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".flac") as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    output_text = transcriber(temp_audio_path)
    content = output_text["text"]

    return content
