import json
import time
from openai import OpenAI
import streamlit as st
from pathlib import Path
import os

API_KEY = os.getenv("api_key")

client = OpenAI(api_key=API_KEY)

def generate_audio(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    file_path = Path(__file__).parent.parent / "tmp/output.mp3"

    response.stream_to_file(file_path)

    return file_path

def generate_image(text):

    response = client.images.generate(
        model="dall-e-2",
        prompt=text,
        n=1,
        size="256x256"
    )

    return response.data[0].url

def generate_story(prompt, context):
    try:

        with st.chat_message("user"):
            st.session_state.history.append({"role": "user", "content": prompt})
            st.write(prompt)

        with st.chat_message("assistant"):
            field = st.info("Génération de l'histoire...")

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Tu es un narrateur qui raconte une histoire interactive sans choix d'un paragraphe de 5 lignes. Tu peux recevoir un contexte et un choix de suite."},
                    {"role": "user", "content": context},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=500,
                stream=True
            )

            full_text = ""
            tokens = []
            for token in response:
                if token.choices and len(token.choices) > 0 and token.choices[0].delta.content is not None:
                    tokens.append(token.choices[0].delta.content)
                    token_text = token.choices[0].delta.content
                    full_text += token_text

            field.info("Synthèse vocale...")
            audio_path = generate_audio(full_text)

            field.info("Génère une image...")
            image = generate_image(full_text[:100])

            st.audio(audio_path, autoplay=True)

            text_container = st.empty()

            st.image(image)

            text = ""
            for token in tokens:
                text += token
                text_container.markdown(text)
                time.sleep(0.150)

            st.session_state.history.append({"role": "assistant", "content": full_text})

            field.empty()

        return full_text
    except Exception as e:
        return f"Une erreur s'est produite : {e}"
    
def generate_choices(context):
    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": (
                    "Tu es un narrateur qui génère exactement trois choix sous format de liste valide. "
                    "Assure-toi que la réponse soit au format list uniquement, sans aucun texte superflu ni markdown."
                    "Exemple de format list Valide:"
                    "Aller à la forêt, Aller à la cuisine, Aller au jardin"
                )},
                {"role": "user", "content": context},
            ],
            max_tokens=300,
        )

        return response.choices[0].message.content.split(', ')
    
    except Exception as e:
        st.error(f"Erreur dans la génération des choix : {e}")
        return [{"id": "error", "description": f"Erreur dans la génération des choix : {e}", "action": ""}]

st.title("Histoire dont vous êtes le héros")
st.write("Bienvenue dans une aventure interactive ! Faites vos choix pour avancer dans l'histoire.")

if 'history' not in st.session_state:
    st.session_state.history = []

if 'choices' not in st.session_state:
    st.session_state.choices = []

for log in st.session_state.history:
    with st.chat_message(log["role"]):
        st.write(log["content"])

if 'context' not in st.session_state:
    context = st.text_input("Entrez le début de votre histoire", placeholder="L'histoire commence dans un village paisible, mais une menace se profile à l'horizon.")
    if context and context.strip() != "":
        st.session_state.context = context
        st.session_state.context += f"\n\n{generate_story(context, st.session_state.context)}"
        st.session_state.choices = generate_choices(st.session_state.context)

if st.session_state.choices and len(st.session_state.choices) > 0:
    cols = st.columns(len(st.session_state.choices))
    for idx, choice in enumerate(st.session_state.choices):
        if cols[idx].button(choice):
            st.session_state.context += f"\n\n{generate_story(choice, st.session_state.context)}"
            st.session_state.choices = generate_choices(st.session_state.context)
            st.rerun()