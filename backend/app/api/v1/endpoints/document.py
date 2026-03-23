from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.deps import get_db
from app.api.deps import get_current_user
from app.services.document_service import DocumentService
from app.models.user import User

router = APIRouter()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await DocumentService.upload_document(db, file, current_user)