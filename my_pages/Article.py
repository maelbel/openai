from openai import OpenAI;
import os
import re

import streamlit as st

API_KEY = os.getenv("api_key")

client = OpenAI(api_key=API_KEY)

def generate_article(content):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant qui rédige des articles intéressants en 2 parties titrées, sans sous partie en utilisant du markdown."},
            {"role": "user", "content": f"Rédige un article détaillé et structuré sur : {content}."}
        ],
        max_tokens = 2000
    )

    return completion.choices[0].message.content

def generate_image(content):

    response = client.images.generate(
        model="dall-e-3",
        prompt=content,
        n=1,
        size="1792x1024"
    )

    return response.data[0].url

def is_title(text):
    """ Détermine si une ligne est un titre. """
    return (len(text) <= 100) and re.search("^#", text)

def openai_create_article(content):

    with (st.chat_message("user")):
        st.write(content)

    with (st.chat_message("assistant")):

        field = st.info("Génération de l'article en cours...")

        article_text = generate_article(content)

        paragraphs = article_text.split("\n\n")

        for paragraph in paragraphs:
            if paragraph.strip() == 0:
                continue

            field.empty()

            st.markdown(paragraph)

            if is_title(paragraph):
                image_prompt = f"Illustration pour : {paragraph}"
                field = st.info(f"Génération de l'image pour : {paragraph}")
                image_url = generate_image(image_prompt)
                st.image(image_url, caption=paragraph)

        field.empty()

value = st.chat_input("Say something")

if (value and value != ""):
    openai_create_article(value)
    value = ""