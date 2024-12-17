from openai import OpenAI;
import os

import streamlit as st

API_KEY = os.getenv("api_key")

client = OpenAI(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

def openai_create_image(content):
    with (st.chat_message("user")):
        st.session_state.messages.append({"role": "user", "content": content})
        st.write(content)

    with (st.chat_message("assistant")):
        field = st.text("Waiting for an answer...")

        response = client.images.generate(
            model="dall-e-2",
            prompt=content,
            n=1,
            size="256x256"
        )

        st.session_state.messages.append({"role": "assistant", "content": response.data[0].url})

        field.image(response.data[0].url)

def openai_create_image_variation(image, content):
    with (st.chat_message("user")):
        st.session_state.messages.append({"role": "user", "content": content})
        st.session_state.messages.append({"role": "user", "content": image})
        st.write(content)
        st.image(image)

    with (st.chat_message("assistant")):
        field = st.text("Waiting for an answer...")

        response = client.images.create_variation(
            image=image,
            n=1,
            size="256x256"
        )

        st.session_state.messages.append({"role": "assistant", "content": response.data[0].url})

        field.image(response.data[0].url)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if (message["role"] == "assistant"):
            st.image(message["content"])
        if (message["role"] == "user"):
            st.text(message["content"])

value = st.chat_input("Say something")
uploaded_file = st.file_uploader("Choose a file", type=["png"])

if ((value and value != "") and uploaded_file is not None):
    openai_create_image_variation(uploaded_file, value)
    value = ""

if ((value and value != "") and uploaded_file is None):
    openai_create_image(value)
    value = ""