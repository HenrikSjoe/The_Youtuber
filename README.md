# 🎥 The Youtuber - RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that enables users to ask questions about data engineering video tutorials. Built with PydanticAI, FastAPI, LanceDB, and Streamlit.

## 📋 Project Overview

This project creates an AI-powered assistant that answers questions based on video transcripts from data engineering tutorials. The chatbot uses vector search to find relevant content and generates educational responses using Google's Gemini model.

**Topics covered in the knowledge base:**
- SQL Analytics with DuckDB
- Python fundamentals & OOP
- FastAPI & API development
- Modern data stack (dbt, dlt, Docker)
- Pydantic & PydanticAI
- Machine Learning (Logistic Regression, XGBoost)
- Azure & Cloud deployment
- And more!

## 🏗️ Architecture

```
User Question
     ↓
[Streamlit Frontend] → [FastAPI Backend] → [PydanticAI Agent]
                                                 ↓
                                          [LanceDB Vector DB]
                                                 ↓
                                          [Video Transcripts]
                                                 ↓
                                          [Gemini 2.5 Flash]
                                                 ↓
                                            Response
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HenrikSjoe/The_Youtuber.git
   cd The_Youtuber
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run data ingestion** (First time only)
   ```bash
   uv run python ingestion.py
   ```

   This will:
   - Create a LanceDB vector database
   - Process all video transcripts
   - Generate embeddings using Google's Gemini embedding model
   - Takes ~10 minutes due to API rate limits

### Running the Application

1. **Start the FastAPI backend**
   ```bash
   uv run uvicorn api:app --reload
   ```
   API will be available at `http://127.0.0.1:8000`

   Interactive API docs: `http://127.0.0.1:8000/docs`

2. **Start the Streamlit frontend** (in a new terminal)
   ```bash
   uv run streamlit run frontend/app.py
   ```
   Frontend will open automatically at `http://localhost:8501`

## 📸 Screenshots

### Streamlit Interface
![Streamlit Frontend](assets/streamlit_demo.png)
*Ask questions about data engineering topics*

### API Documentation
![FastAPI Docs](assets/api_docs.png)
*Interactive API documentation with Swagger UI*

### Example Query
**Question:** "Tell me about OOP"

**Response:**
> Object-Oriented Programming (OOP) in Python revolves around classes, which act as blueprints for creating instances or objects. When you instantiate a class, the `__init__` method runs first, allowing you to define initial attributes for your object...
>
> **Source Video:** Python_oop_1

## 📁 Project Structure

```
The_Youtuber/
├── backend/
│   ├── constants.py        # Path configurations
│   ├── data_models.py      # Pydantic models
│   └── rag.py             # RAG agent logic
├── data/                   # Video transcript files (.md)
├── frontend/
│   └── app.py             # Streamlit UI
├── knowledge_base/         # LanceDB vector database
├── api.py                 # FastAPI endpoints
├── ingestion.py           # Data ingestion script
├── .env                   # Environment variables
├── pyproject.toml         # Project dependencies
└── README.md
```

## 🛠️ Technologies Used

- **PydanticAI**: AI agent framework with structured outputs
- **FastAPI**: High-performance API framework
- **Streamlit**: Interactive web frontend
- **LanceDB**: Vector database for embeddings
- **Google Gemini**: LLM and embedding model
- **Python 3.11**: Core programming language
- **uv**: Fast Python package manager

## 🔧 API Endpoints

### `GET /`
Health check and API information

### `POST /rag/query`
Query the RAG chatbot

**Request Body:**
```json
{
  "prompt": "How do I setup DuckDB?"
}
```

**Response:**
```json
{
  "video_title": "SQL analytics course with DuckDB - setup duckdb",
  "filepath": "/path/to/transcript.md",
  "answer": "Detailed answer based on video content..."
}
```

## 📚 Key Features

- ✅ Vector-based semantic search
- ✅ Context-aware responses
- ✅ Source attribution (cites video sources)
- ✅ Educational tone matching The Youtuber's style
- ✅ Fast retrieval with LanceDB
- ✅ Interactive web interface
- ✅ RESTful API

## 🧪 Example Queries

Try asking:
- "How do I setup DuckDB?"
- "Explain Python OOP concepts"
- "What is FastAPI?"
- "How do I use Pydantic?"
- "Tell me about Docker"

## 📝 Notes

- First-time ingestion takes ~10 minutes due to Google API rate limits
- The system uses `gemini-2.5-flash` for generation and `gemini-embedding-001` for embeddings
- Responses are limited to 6 sentences for clarity

## 📄 License

This project is for educational purposes as part of an AI Engineering course.
