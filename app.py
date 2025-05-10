from flask import Flask, request, jsonify
from transformers import pipeline
import gradio as gr

app = Flask(__name__)

# Chatbot modelini yükle
chatbot = pipeline("text-generation", model="facebook/xglm-564M")

# Chatbot yanıtı üreten fonksiyon
def respond(user_input):
    response = chatbot(user_input, max_length=100)[0]["generated_text"]
    return response

# Gradio arayüzü
iface = gr.Interface(
    fn=respond,
    inputs=gr.Textbox(label="Mesajınızı yazın (herhangi bir dilde)"),
    outputs="text",
    title="Çok Dilli Chatbot",
    description="Türkçe, İngilizce veya başka bir dilde sohbet edin!"
)

# Flask route’ları
@app.route('/')
def home():
    return iface.launch(share=False)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)