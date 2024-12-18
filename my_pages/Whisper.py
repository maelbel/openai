from openai import OpenAI
import streamlit as st
from pathlib import Path
import os

API_KEY = os.getenv("api_key")

client = OpenAI(api_key=API_KEY)

whisper, tts, wtgtt = st.tabs(["Audio", "Text to Speech", "Whisper to GPT to TTS"])

# Whisper
audio = whisper.audio_input("Dites quelque chose", key="whisper")

if (audio):
    file_path = Path(__file__).parent.parent / "tmp/input.mp3"

    with open(file_path, "wb") as file:
        file.write(audio.getbuffer())

    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(file=file, model="whisper-1")

        whisper.write(transcription.text)

# Text to Speech
value = tts.text_input("Votre prompt")

if (value):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=value
    )

    file_path = Path(__file__).parent.parent / "tmp/output.mp3"

    response.stream_to_file(file_path)

    tts.audio(file_path, autoplay=True)

# Whisper to GPT to TTS
audio = wtgtt.audio_input("Dites quelque chose", key="wtgtt")

option = wtgtt.selectbox(
    "Voice speech",
    ("Alloy", "Echo", "Fable", "Onyx", "Nova", "Shimmer"),
    index=0,
)

if (audio and option):

    field = wtgtt.info("Transcription de l'audio...")

    file_path = Path(__file__).parent.parent / "tmp/input.mp3"

    with open(file_path, "wb") as file:
        file.write(audio.getbuffer())

    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(file=file, model="whisper-1")

    user_chat = wtgtt.chat_message("user")
    user_chat.write(transcription.text)
    
    field.info("Traitement de la transcription...")

    assistant_chat = wtgtt.chat_message("assistant")

    text = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant utile avec humour et gentillesse et une voix adapté pour l'oral. Tu dois ajouter des balises SSML pour avoir un ton dynamique, enjoué et convivial."},
            {"role": "user", "content": transcription.text}
        ],
        max_tokens = 2000
    )

    if(text):
        field.info("Synthèse vocale...")
        speech = client.audio.speech.create(
            model="tts-1",
            voice=option.lower(),
            input= text.choices[0].message.content
        )

        print(text.choices[0].message.content)

        file_path = Path(__file__).parent.parent / "tmp/output.mp3"

        speech.stream_to_file(file_path)

        assistant_chat.audio(file_path, autoplay=True)

    field.empty()