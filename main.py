import streamlit as st

path = "./my_pages/"

pg = st.navigation([
    st.Page(path + "Home.py", icon=":material/home:"),
    st.Page(path + "OpenAI.py", title="1. API OpenAI"),
    st.Page(path + "DALL-E.py", title="2. API DALL-E 2"),
    st.Page(path + "Article.py", title="3. Article"),
    st.Page(path + "Stream.py", title="4. Stream"),
    st.Page(path + "Whisper.py", title="5. Whisper"),
    st.Page(path + "Fine-tuning.py", title="6. Fine-tuning"),
    st.Page(path + "History.py", title="7. Histoire dont vous êtes le héros"),
])

pg.run()