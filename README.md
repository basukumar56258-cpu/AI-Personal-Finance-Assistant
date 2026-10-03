# 💰 AI Personal Finance Assistant

Professional LLM-ready finance project for income/expense analysis, budgets, savings insights and AI financial Q&A.

## Architecture
```text
Frontend (React + Tailwind)
        ↓ REST API
Backend (Python + FastAPI)
        ↓
Finance Analytics + Budget Services
        ↓
LLM (OpenAI / Gemini / Ollama)
        ↓
AI Insights & Assistant
        ↓
SQLite / PostgreSQL
```

## GitHub Structure
```text
AI-Personal-Finance-Assistant/
├── frontend/                 # React + Tailwind frontend
├── backend/
│   └── app/
│       ├── ai/               # LLM + prompts + insights
│       ├── api/              # FastAPI routes
│       ├── database/         # database layer
│       ├── schemas/          # Pydantic models
│       └── services/         # finance logic
├── data/
├── tests/
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

API:
```bash
uvicorn backend.app.main:app --reload
```
Docs: http://127.0.0.1:8000/docs

## LLM
Add an API key to `.env` and connect the provider call in `backend/app/ai/llm.py`.
Recommended: OpenAI, Gemini, or Ollama.

Educational project only; it does not replace a qualified financial adviser.
