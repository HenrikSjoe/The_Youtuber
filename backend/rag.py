from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DATABASE_PATH
import lancedb

vector_db = lancedb.connect(uri=VECTOR_DATABASE_PATH)

rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        "You are The Youtuber - a passionate data engineering educator who teaches through video tutorials. ",
        "You have a friendly, enthusiastic teaching style and love helping people learn data engineering, SQL, Python, FastAPI, Azure and cloud technologies. ",
        "Always answer based on the retrieved video transcript knowledge. ",
        "Don't hallucinate, rather say you can't answer it if the user prompts outside of the retrieved knowledge",
        "Keep answers clear, practical and educational - max 6 sentences. ",
        "Always mention which video the answer comes from.",
    ),
    output_type=RagResponse
)

@rag_agent.tool_plain
def retrieve_top_documents(query: str, k=3) -> str:
    """
    Uses vector search to find the closest k matching video transcripts to the query
    """
    results = vector_db["transcripts"].search(query=query).limit(k).to_list()
    top_result = results[0]

    return f"""
    Video Title: {top_result["filename"]},
    Filepath: {top_result["filepath"]},
    Content: {top_result["content"]}
    """