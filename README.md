# PDF RAG Chatbot 📄🤖

An AI chatbot powered by **Gemini 1.5 Flash** that answers questions based on the content of a PDF file using Retrieval-Augmented Generation (RAG).  
The bot automatically downloads the PDF from a given URL, extracts the text, and uses it as context for accurate, document-based answers.

---

## 🚀 Features
- Retrieval-Augmented Generation from a PDF file.
- Automatically fetches and processes the document.
- Avoids giving incorrect answers when information is not found.
- Clean **Gradio** interface with custom branding.

---

## 📂 Project Structure
```plaintext
PDF-RAG-Chatbot/
│
├── app.py         # Gradio interface for the chatbot
├── rag_pdf.py     # RAG logic for PDF content extraction and Q&A
├── requirements.txt # Dependencies for the project
└── README.md      # Project documentation
