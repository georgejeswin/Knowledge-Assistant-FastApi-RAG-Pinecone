from app.workers.celery_app import celery_app
import asyncio

from app.services.rag.rag_service import RagService
from app.db.session import AsyncSessionLocal
from app.models.document import Document
from sqlalchemy import select


@celery_app.task
def process_document(document_id: int):

    async def run():
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(Document).where(Document.id == document_id)
            )
            document = result.scalar_one()

            if not document:
                return
            
            await RagService.index_document(document)

    asyncio.run(run())