from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.chat import ChatMessage


class ChatRepository:

    @staticmethod
    async def create(db: AsyncSession, user_id: int, role: str, content: str):
        msg = ChatMessage(user_id=user_id, role=role, content=content)
        db.add(msg)
        await db.commit()
        await db.refresh(msg)
        return msg

    @staticmethod
    async def get_recent(db: AsyncSession, user_id: int, limit=100):
        result = await db.execute(
            select(ChatMessage)
            .where(ChatMessage.user_id == user_id)
            .order_by(ChatMessage.id.asc())
            # .limit(limit)
        )
        return list(result.scalars())