import streamlit as st
from utils.asr_utils import transcribe_audio
from utils.scam_utils import predict_scam

st.set_page_config(page_title="Scam Audio Detection App")

st.title("Scam Audio Detection App")
st.write("Upload an audio file, convert it to text, and detect whether it is a scam.")

st.info("⚠️ Please upload audio in FLAC format. Other formats are not supported.")

uploaded_file = st.file_uploader(
    "Upload a FLAC audio file",
    type=["flac"]
)

if uploaded_file is not None:
    st.audio(uploaded_file)

    # 👉 Debug: 检查上传是否正常
    st.write("File uploaded successfully")
    st.write("Name:", uploaded_file.name)
    st.write("Type:", uploaded_file.type)
    st.write("Size:", uploaded_file.size)

    # 👉 暂时先不做 ASR
    # with st.spinner("Transcribing audio..."):
    #     text = transcribe_audio(uploaded_file)

    # st.subheader("Transcribed Text")
    # st.write(text)

    st.warning("ASR temporarily disabled for debugging")
