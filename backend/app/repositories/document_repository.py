from sqlalchemy.ext.asyncio import AsyncSession
from app.models.document import Document


class DocumentRepository:

    @staticmethod
    async def create(db: AsyncSession, filename: str, content: str, owner_id: int):
        doc = Document(
            filename=filename,
            content=content,
            owner_id=owner_id
        )
        db.add(doc)
        await db.commit()
        await db.refresh(doc)
        return doc