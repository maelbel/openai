import streamlit as st

# Titre principal
st.title("📑 Formation OpenAI")

# Créer un sommaire avec des liens internes
st.header("Sommaire")
st.markdown("""
1. [Introduction](#introduction)
2. [Section 1 : API OpenAI](#section-1-contexte)
3. [Section 2 : API DALL-E](#section-2-developpement)
4. [Section 3 : Article](#section-3-conclusion)
5. [Section 4 : Stream](#section-4-stream)
6. [Section 5 : Whisper](#section-5-whisper)
""")

# Sections du contenu
st.header("Introduction")
st.write("Bienvenue dans ce document généré avec Streamlit. Cette section introduit le sujet abordé...")

st.header("Section 1 : Contexte")
st.write("Dans cette section, nous discutons du contexte global du sujet et des points importants...")

st.header("Section 2 : Développement")
st.write("Voici le cœur du document avec les explications principales et les arguments détaillés...")

st.header("Section 3 : Conclusion")
st.write("Ici, nous résumons les points principaux et tirons une conclusion sur le sujet.")

st.header("Références")
st.write("Liste des sources et références utilisées dans ce document...")