import gradio as gr
from transformers import pipeline

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

# Vercel için port ayarı
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)