from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'API de détection de mots interdits !"

@app.route('/check', methods=['POST'])
def check_forbidden_words():
    # Récupérer les données de la requête
    data = request.json
    response_text = data.get("response", "").lower()  # Convertir le texte en minuscules
    forbidden_words = [word.lower() for word in data.get("forbiddenWords", [])]  # Convertir les mots interdits en minuscules

    # Vérifier les mots interdits dans le texte
    violations = [word for word in forbidden_words if f" {word} " in f" {response_text} "]

    # Retourner une alerte si des mots interdits sont détectés
    if violations:
        return jsonify({
            "alert": f"⚠️ Mots interdits détectés : {', '.join(violations)}.",
            "valid": False
        })

    # Retourner une validation si aucun mot interdit n'est détecté
    return jsonify({
        "alert": "✅ Aucun mot interdit détecté.",
        "valid": True
    })

if __name__ == "__main__":
    # Définir le port à partir des variables d'environnement ou utiliser 5000 par défaut
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
