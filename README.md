# AI-Agent
# 🤖 Agentic AI Researcher (2026 Edition)

A local, private AI agent built with **LangGraph** and **Ollama**. It can autonomously decide whether to search Wikipedia for facts or use the live web for news to answer your questions.

## 🛠️ Requirements
- **Python 3.10+**
- **Ollama** (Running locally)
- **Llama 3.1** model (supports tool-calling)

## 📥 Installation

### 1. Setup Ollama
If you haven't installed Ollama yet, download it from [ollama.com](https://ollama.com).
After installation, open your terminal and run:
```bash
# Start the local server
ollama serve

# In a different terminal, download the model
ollama pull llama3.1
