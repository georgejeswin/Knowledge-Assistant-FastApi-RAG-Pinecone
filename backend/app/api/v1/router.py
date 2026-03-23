from fastapi import APIRouter
from app.api.v1.endpoints import auth
from app.api.v1.endpoints import user
from app.api.v1.endpoints import document

api_router = APIRouter()

@api_router.get("/health")
async def health():
    return {"status": "ok"}

api_router.include_router(auth.router, prefix = "/auth", tags = ["auth"])
api_router.include_router(user.router, prefix = "/user", tags = ["user"])
api_router.include_router(document.router, prefix = "/document", tags = ["document"])