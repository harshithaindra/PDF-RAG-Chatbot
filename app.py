import gradio as gr
from rag_pdf import get_response
import json
import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 'branding.json'))) as f:
    brand_info = json.load(f)['brand']

with gr.Blocks(title=brand_info["organizationName"]) as demo:
    
    gr.HTML(
        f"<div style='display: flex; align-items: center; justify-content: center; margin-bottom: 20px;'>"
        f"<img src='{brand_info['logo']['title']}' alt='{brand_info['organizationName']} Logo' style='height: 100px;'>"
        "</div>"
    )
    gr.ChatInterface(
        fn=get_response,
        chatbot=gr.Chatbot(height=500, avatar_images=brand_info["chatbot"]["avatar"]),
        type="messages",
        title=brand_info["organizationName"],
        description=brand_info["slogan"],
        examples=[
            ["who is the cto?", []],
            ["Who is madam deepti?", []],
            ["What are the courses offfered by heareandnowai?", []]
        ],
    )

if __name__ == "__main__":
    demo.launch()








