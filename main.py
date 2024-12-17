import streamlit as st

path = "./pages/"

pg = st.navigation([
    st.Page(path + "Home.py", icon=":material/home:"),
    st.Page(path + "NLP.py", title="1. Natural Language Processing (NLP)"),
    st.Page(path + "OpenAI.py", title="2. API OpenAI"),
    st.Page(path + "DALL-E.py", title="3. API DALL-E 2"),

    st.Page(path + "Whisper.py", title="4. Whisper"),
    st.Page(path + "Fine-tuning.py", title="5. Fine-tuning"),
    st.Page(path + "Exercise.py", title="6. Exercice final"),
])

pg.run()