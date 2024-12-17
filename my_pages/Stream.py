import time
from openai import OpenAI;
import os

import streamlit as st

API_KEY = os.getenv("api_key")

client = OpenAI(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

def new_message(content: str):
    with (st.chat_message("user")):
        st.session_state.messages.append({"role": "user", "content": content})
        st.write(content)

    with (st.chat_message("assistant")):

        text_container = st.empty()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tu es un assistant utile."},
                {"role": "user", "content": content}
            ],
            stream=True
        )


        full_text = ""
        for token in response:
            if token.choices and len(token.choices) > 0 and token.choices[0].delta.content is not None:
                chunk_text = token.choices[0].delta.content
                full_text += chunk_text
                text_container.markdown(full_text)
                time.sleep(0.1)

        st.session_state.messages.append({"role": "assistant", "content": full_text})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.text(message["content"])

st.info("Interface utilisateur en temps réel")

value = st.chat_input("Say something")

if (value and value != ""):
    new_message(value)
    value = ""