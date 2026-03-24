from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.services.rag.rag_service import RagService
from app.services.llm.llm_service import LLMService

router = APIRouter()


@router.get("/chat")
async def chat(query: str):

    async def event_generator():
        contexts = await RagService.query(query)

        prompt = f"""
        Answer ONLY from the context below.

        Context:
        {contexts}

        Question:
        {query}
        """

        async for chunk in LLMService.stream_response(prompt):
            yield chunk

    return StreamingResponse(event_generator(), media_type="text/plain")