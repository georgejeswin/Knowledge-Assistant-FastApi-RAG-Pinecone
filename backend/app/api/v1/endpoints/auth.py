from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate
from app.db.deps import get_db
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await AuthService.register(db, user.email, user.password)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    return await AuthService.login(db, form_data.username, form_data.password)