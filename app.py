import streamlit as st
from utils.asr_utils import transcribe_audio
from utils.scam_utils import predict_scam

st.set_page_config(page_title="Scam Audio Detection App")

st.title("Scam Audio Detection App")
st.write("Upload an audio file, convert it to text, and detect whether it is a scam.")

st.info("⚠️ Please upload audio in FLAC format. Other formats are not supported.")


def format_prediction_message(prediction):
    pred = prediction.strip().lower()

    if pred == "scam":
        return (
            "Scam",
            "This audio is likely a scam.\n\n"
            "Do not share any personal or financial information, such as bank details, passwords, "
            "or verification codes. Avoid taking any immediate action requested in the message, "
            "and verify the source through official channels if needed."
        )
    else:
        return (
            "Not Scam",
            "This audio does not appear to be a scam.\n\n"
            "You may continue the conversation, but remain cautious if sensitive personal or "
            "financial information is involved."
        )


uploaded_file = st.file_uploader(
    "Upload a FLAC audio file",
    type=["flac"]
)

if uploaded_file is not None:
    st.audio(uploaded_file)

    with st.spinner("Transcribing audio..."):
        text = transcribe_audio(uploaded_file)

    st.subheader("Transcribed Text")
    st.write(text)

    with st.spinner("Detecting scam..."):
        prediction = predict_scam(text)

    label, message = format_prediction_message(prediction)

    st.subheader("Prediction")

    if label == "Scam":
        st.error(f"🚨 {label}")
        st.warning(message)
    else:
        st.success(f"✅ {label}")
        st.info(message)
