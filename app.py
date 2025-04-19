import streamlit as st
import os
from datetime import datetime
from interpreteur import interpreter_reve

# Charger le fichier des rêves sauvegardés
dreams_file = "dreams.txt"

# Fonction pour sauvegarder les rêves dans un fichier
def save_dream(dream_text, interpretation):
    with open(dreams_file, "a") as f:
        f.write(f"{datetime.now()} - Rêve: {dream_text} - Interprétation: {interpretation}\n")

# Sidebar pour afficher la liste des rêves passés
st.sidebar.header("Rêves passés 🌙")
if os.path.exists(dreams_file):
    with open(dreams_file, "r") as f:
        dreams = f.readlines()
        for dream in dreams[-5:]:  # Afficher les 5 derniers rêves
            st.sidebar.text(dream)
else:
    st.sidebar.text("Aucun rêve enregistré.")

# Ajouter un fond étoilé en CSS
st.markdown(
    """
    <style>
    body {
        background: url('https://th.bing.com/th/id/R.0a643237cbb7d48899d2b9764631de44?rik=EpcvwjqMQyeH2Q&riu=http%3a%2f%2fke-du-bonheur.fr%2fwp-content%2fuploads%2f2015%2f02%2fsource.jpg&ehk=gXrb6IbTyUlnvu90H7olQhJ9Uqyn5BiIQ%2fcfpVEKAzE%3d&risl=&pid=ImgRaw&r=0') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Ajouter de la musique d'ambiance
st.markdown("### Écoute la musique d'ambiance 🎶")
audio_file = open("musique_ambiance.mp3", "rb")
st.audio(audio_file, format="audio/mp3", start_time=0)

# Animations et effets CSS
st.markdown(
    """
    <style>
    .css-18e3th9 {
        animation: fadeIn 2s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .css-1v0mbdj {
        transition: transform 1s ease;
    }

    .css-1v0mbdj:hover {
        transform: scale(1.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Personnaliser l'affichage pour mobile
st.markdown(
    """
    <style>
    .css-1v0mbdj {
        padding: 10px;
        font-size: 18px;
    }

    @media (max-width: 600px) {
        .css-1v0mbdj {
            font-size: 14px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Interface principale
st.title("🌌 Interprétation mystique de tes rêves")
st.write("Raconte-moi ton rêve, et je t'en livrerai la signification cachée... 🧙‍♂️")
texte_reve = st.text_area("Décris ton rêve ici :")

if st.button("Interpréter"):
    if texte_reve:
        interpretation = interpreter_reve(texte_reve)
        st.write(f"Voici l'interprétation :\n\n{interpretation}")
        save_dream(texte_reve, interpretation)  # Sauvegarde du rêve et de son interprétation
    else:
        st.write("Entrez un rêve à interpréter.")
