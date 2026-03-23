import streamlit as st
from utils import generate_script
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Video Script Generator")

with st.sidebar:
    preload_key = os.getenv("OPENAI_API_KEY")
    openai_api_key = st.text_input("Enter OpenAI API Key: ", type="password", value=preload_key)
    st.markdown("[Get your API Key here](https://platform.openai.com/api-keys)")

subject = st.text_input("Enter a title for the video")
video_length = st.number_input("Enter a duration in Minutes", min_value=0.1, step=0.1)
creativity = st.slider("Enter the creativity for the generator", min_value=0.0, max_value=1.0, value=0.2, step=0.1)

submit = st.button("Generate script")

if submit and not openai_api_key:
    st.info("OpenAI API key is required")
    st.stop()

if submit and not subject:
    st.info("Title is required")
    st.stop()

if submit and not video_length >= 0.1:
    st.info("Video length is required to be longer or equal to 0.1")
    st.stop()

if submit:
    with st.spinner("Generating script..."):
        search_result , title, script = generate_script(
            subject,
            creativity,
            video_length,
            api_key=""
        )
    st.success("Script generated!")
    st.subheader("Title:")
    st.write(title)
    st.subheader("Script:")
    st.write(script)

    with st.expander("Wikipedia result"):
        st.info(search_result)