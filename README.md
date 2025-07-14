# 🤖 Agentic AI Assistant

This is a multi-modal AI assistant that answers user queries using:
- 📄 PDF documents (local course material)
- 🌐 Web search via Tavily
- 🔍 Observability using LangSmith
- 🧠 LLMs via Groq's LLaMA3 model
- 📚 Vector search using FAISS + HuggingFace embeddings

---

## 🛠️ Tech Stack
- Python
- LangChain
- FastAPI (Backend)
- Streamlit (Frontend)
- FAISS + HuggingFace (Embeddings)
- Tavily (Web Search)
- LangSmith (Tracing/Observability)
- Groq LLaMA3 (LLM provider)

---

## 📁 Project Structure

```
final_project/
│
├── agent.py        # Main agent logic with tools
├── app.py          # Streamlit frontend
├── main.py         # FastAPI backend
├── rag.py
├── utils.py
├── api.py          # Supporting code
├── vectorstore/    # Saved vector DB (FAISS)
├── data/           # Raw PDF files
├── .env            # API keys (not shared)
└── README.md       # This file
```

---

## 🚀 How to Run Locally

### 1. Clone the project

```bash
git clone <your-repo-url>
cd final_project
```

### 2. Add your `.env` file

Create a `.env` file in the root and add:

```ini
GROQ_API_KEY=your_key
LANGSMITH_API_KEY=your_key
TAVILY_API_KEY=your_key
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI backend

```bash
uvicorn main:app --reload
```

### 5. In a second terminal, run the Streamlit frontend

```bash
streamlit run app.py
```

---

## 💬 Sample Q&A

> **Q:** What is importance of rheology?  
> **A:** Rheology provides a foundational understanding of material behavior and is critical for modeling biological structures and improving industrial processes.

---

## ✅ Submission Ready

- ✔️ Fully working: PDF + Web + Agent + LangSmith  
- ✔️ Frontend + Backend connected  
- ✔️ Ready to submit on GitHub and Google Classroom
