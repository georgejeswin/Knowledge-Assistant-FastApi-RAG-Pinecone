from fastapi import APIRouter
from app.services.rag.rag_service import RagService

router = APIRouter()
@router.post("/chat")
async def chat(query: str):
    contexts = await RagService.query(query)

    prompt = f"""
    Answer based on context:

    {contexts}

    Question: {query}
    """

    return {"answer": prompt}