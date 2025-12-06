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
[Streamlit Frontend] → [Azure Functions API] → [PydanticAI Agent]
                                                      ↓
                                               [LanceDB Vector DB]
                                                      ↓
                                               [Video Transcripts]
                                                      ↓
                                               [Gemini 2.5 Flash]
                                                      ↓
                                                  Response
```

**Deployment:**
- Backend: Azure Functions (serverless)
- Frontend: Can be run locally or deployed
- Database: LanceDB vector database (file-based)

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
   FUNCTION_APP_API=your_azure_function_api_key_here
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

**Option 1: Use the deployed Azure Functions API (Recommended)**
   ```bash
   uv run streamlit run frontend/app.py
   ```
   Frontend will open automatically at `http://localhost:8501`

   The app connects to the live Azure Functions API automatically.

**Option 2: Local development with FastAPI**

   For local development and testing:

   1. Start the FastAPI backend:
      ```bash
      uv run uvicorn api:app --reload
      ```
      API available at `http://127.0.0.1:8000`

   2. Update [frontend/app.py](frontend/app.py) to use local endpoint:
      ```python
      url = "http://127.0.0.1:8000/rag/query"
      ```

   3. Start Streamlit:
      ```bash
      uv run streamlit run frontend/app.py
      ```

## 💡 Example Usage
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
│   └── app.py             # Streamlit UI (connects to Azure)
├── knowledge_base/         # LanceDB vector database
├── api.py                 # FastAPI endpoints (local dev)
├── function_app.py        # Azure Functions entry point
├── host.json              # Azure Functions configuration
├── requirements.txt       # Azure Functions dependencies
├── ingestion.py           # Data ingestion script
├── .env                   # Environment variables
├── pyproject.toml         # Project dependencies
└── README.md
```

## 🛠️ Technologies Used

- **PydanticAI**: AI agent framework with structured outputs
- **Azure Functions**: Serverless backend deployment
- **FastAPI**: High-performance API framework (local dev)
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
- ✅ Serverless deployment on Azure Functions
- ✅ Cloud-based accessibility

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

## ☁️ Deployment

The application is deployed on **Azure Functions** for serverless backend hosting.

**Live API:** `https://the-youtuber-hs-de24.azurewebsites.net`

**Deployment steps:**
1. Set up Azure Functions app
2. Configure environment variables (`GOOGLE_API_KEY`) in Azure Portal
3. Deploy using Azure Functions Core Tools or VS Code extension
4. Upload `knowledge_base/` directory to Azure storage or include in deployment

The frontend Streamlit app connects to the Azure Functions API using the `FUNCTION_APP_API` key for authentication.

## 📄 License

This project is for educational purposes as part of an AI Engineering course.
