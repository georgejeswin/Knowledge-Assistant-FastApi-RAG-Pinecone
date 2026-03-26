from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.db.deps import get_db
from app.api.deps import get_current_user
from app.services.chat_service import ChatService
from app.repositories.chat_repository import ChatRepository
from app.services.rag.rag_service import RagService
from app.services.llm.llm_service import LLMService
from app.models.user import User

router = APIRouter()

@router.post("/")
async def chat(
    request: dict,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    message = request["message"]

    async def event_generator():

        # Save user message
        await ChatRepository.create(db, user.id, "user", message)

        # Build prompt
        prompt = await ChatService.build_prompt(db, user, message)

        response_text = ""

        async for chunk in LLMService.stream_response(prompt):
            response_text += chunk
            yield chunk

        # Save assistant response
        await ChatRepository.create(db, user.id, "assistant", response_text)

    return StreamingResponse(event_generator(), media_type="text/plain")

@router.get("/")
async def chat(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # Get user messages
    messages = await ChatRepository.get_recent(db, user.id)

    return messages