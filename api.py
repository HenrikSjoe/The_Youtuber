from fastapi import FastAPI
from backend.rag import rag_agent
from backend.data_models import Prompt

app = FastAPI(title="The Youtuber RAG API", description="Ask questions about data engineering video tutorials")

@app.get("/")
async def root():
    return {
        "message": "Welcome to The Youtuber RAG API",
        "endpoints": {
            "/rag/query": "POST - Ask questions about video content"
        }
    }

@app.post("/rag/query")
async def query_documentation(query: Prompt):
    result = await rag_agent.run(query.prompt)
    return result.output
