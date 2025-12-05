from pydantic import BaseModel, Field
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from dotenv import load_dotenv 

load_dotenv()
embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

EMBEDDING_DIM = 3072

class VideoTranscript(LanceModel):
    doc_id: str
    filepath: str
    filename: str = Field(description="Video title without file extension")
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()

class Prompt(BaseModel):
    prompt: str = Field(description="User question about video content")

class RagResponse(BaseModel):
    video_title: str = Field(description="Title of the video source")
    filepath: str = Field(description="Path to transcript file")
    answer: str =Field(description="Answer based on video transcript")