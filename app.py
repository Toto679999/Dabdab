from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'API de détection de mots interdits !"

@app.route('/check', methods=['POST'])
def check_forbidden_words():
    data = request.json
    response_text = data.get("response", "")
    forbidden_words = data.get("forbiddenWords", ["concernant", "mauvais", "dangereux"])

    violations = [word for word in forbidden_words if word in response_text]

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

if __name__ == "__main__":
    app.run(debug=True)
