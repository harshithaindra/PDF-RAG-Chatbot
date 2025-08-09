from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import PyPDF2

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
model = "gemini-1.5-flash"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = OpenAI(api_key=api_key, base_url=base_url)

url = "https://raw.githubusercontent.com/hereandnowai/rag-workshop/main/pdfs/About_HERE_AND_NOW_AI.pdf"

url = "https://raw.githubusercontent.com/hereandnowai/rag-workshop/main/pdfs/About_HERE_AND_NOW_AI.pdf"

response = requests.get(url)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(script_dir, "prospect-hereandnowai.pdf")

with open(file_name, "wb") as file:
    file.write(response.content)

try:
    with open(file_name, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text_chunks = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pdf_text_chunks.append(page_text.strip())
        pdf_context = "\n".join(pdf_text_chunks) if pdf_text_chunks else "No text found in PDF."

except Exception as e:
    print(f"Error reading PDF file: {e}")
    pdf_context = "Error reading PDF file."

system_prompt = f"""content from pdf {file_name}:\n {pdf_context}
                answer this question based on the context 
                if you can't find the answer, say don't give wrong information"""

def get_response(user_message , history):
    messages = [{"role":"system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model=model,
        messages=messages)
    return response.choices[0].message.content

if __name__ == "__main__":
    print(get_response("What is HERE AND NOW AI?", [])) 
