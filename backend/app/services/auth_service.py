from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.core.security import create_access_token, hash_password, verify_password

class AuthService:
    @staticmethod
    async def register(db: AsyncSession, email: str, password: str):
        existing = await UserRepository.get_by_email(db, email)
        if existing:
            raise Exception('User exists')
        
        hashed_password = hash_password(password)
        user = await UserRepository.create(db, email, hashed_password)

        token = create_access_token({"sub": user.email})
        
        return { 
            "access_token": token,
            "token_type": "bearer"
        }
    
    @staticmethod
    async def login(db: AsyncSession, email: str, password: str):
        user = await UserRepository.get_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            raise Exception('Invalid Credentials')
        
        token = create_access_token({"sub": user.email})

        return { 
            "access_token": token,
            "token_type": "bearer"
        }