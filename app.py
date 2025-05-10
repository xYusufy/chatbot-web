from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Daha küçük bir model yükle
chatbot = pipeline("text-generation", model="distilgpt2")

# Chatbot yanıtı üreten fonksiyon
def respond(user_input):
    response = chatbot(user_input, max_length=100)[0]["generated_text"]
    return response

# Flask route’ları
@app.route('/')
def home():
    return "Çok Dilli Chatbot - API Çalışıyor! (Arayüz için /chat kullanın)"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    if user_input:
        response = respond(user_input)
        return jsonify({"response": response})
    return jsonify({"error": "Mesaj girin"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
