from flask import Flask, request, jsonify
import os  # Pour accéder aux variables d'environnement

app = Flask(__name__)

# Route principale
@app.route('/')
def home():
    return "Bienvenue sur l'API de détection de mots interdits !"

# Route pour vérifier les mots interdits
@app.route('/check', methods=['POST'])
def check_forbidden_words():
    # Récupérer les données de la requête JSON
    data = request.json
    response_text = data.get("response", "")  # Texte à analyser
    forbidden_words = data.get("forbiddenWords", ["concernant", "mauvais", "dangereux"])  # Liste par défaut

    # Vérifier les mots interdits dans le texte
    violations = [word for word in forbidden_words if word in response_text]

    # Préparer la réponse
    if violations:
        return jsonify({
            "alert": f"⚠️ Mots interdits détectés : {', '.join(violations)}.",
            "valid": False
        })
    else:
        return jsonify({
            "alert": "✅ Aucun mot interdit détecté.",
            "valid": True
        })

# Configurer l'exécution de Flask
if __name__ == "__main__":
    # Récupérer le port de l'environnement ou utiliser 5000 par défaut
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
