Multi-Agent AI Chatbot

Overview
This project implements a **multi-agent conversational chatbot** powered by **FastAPI**, **LangChain**, and **Ollama LLMs**.  
The chatbot routes user queries to specialized agents based on intent classification:

-**AI Agent** → handles questions about artificial intelligence & machine learning  
-**Admission Agent** → answers questions about Concordia University CS admissions  
-**General Agent** → manages casual conversation, greetings, or general topics  

The system also supports **conversation memory**, **CORS-enabled API**, and a **minimal web UI** for interaction.

Tech Stack
- **Backend**: FastAPI, Uvicorn:contentReference[oaicite:0]{index=0}  
- **LLM Framework**: LangChain + Ollama:contentReference[oaicite:1]{index=1}  
- **Vector Store**: FAISS (for memory and retrieval)  
- **Frontend**: Vanilla HTML/CSS/JS (chat interface):contentReference[oaicite:2]{index=2}  
- **Other**: Python 3.9+, Pydantic, CORS middleware  

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-chatbot.git
cd multi-agent-chatbot

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Start the FastAPI Server
uvicorn main:app --reload


