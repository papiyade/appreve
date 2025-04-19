import os
from openai import OpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Initialiser le client OpenAI avec la clé API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpreter_reve(texte_reve):
    prompt = f"""
    Tu es un expert en interprétation des rêves. Voici le rêve d'une personne :

    \"{texte_reve}\"

    Donne une interprétation mystique, symbolique, psychologique et poétique de ce rêve. Parle comme un guide spirituel.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.85
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur : {str(e)}"
