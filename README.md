
# 🤖 AI Chatbot using LangChain + Groq API

This is a simple command-line AI chatbot built using **LangChain**, **Groq API**, and the **Llama 3 model**.  
The chatbot can generate intelligent and context-aware responses while maintaining conversation memory using vector embeddings.
[https://github.com/Komal2008/ChatBOT-using-LLM/blob/main/chatbot.jpeg].
---

## ✨ Features

- 💬 Conversational AI chatbot  
- ⚡ Fast responses using Groq inference  
- 🧠 Memory-based conversation support  
- 🔍 Semantic embeddings using Hugging Face  
- 🗂️ FAISS vector database integration  
- 🖥️ Simple command-line interface  

---

## 🧰 Technologies Used

- Python  
- LangChain  
- Groq API  
- Hugging Face Embeddings  
- FAISS  
- Llama 3  

---

## ⚙️ How It Works

1. User enters a query in the terminal  
2. Query is converted into embeddings  
3. Relevant memory/context is retrieved from FAISS  
4. Context and query are sent to the Llama 3 model  
5. AI generates a contextual response  

---

## 🚀 Run the Project

```bash
pip install -r requirements.txt
python LLM.py
