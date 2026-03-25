from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title = 'Knowledge Assistant')

app.include_router(api_router, prefix='/api/v1')

@app.get('/')
async def root():
    return { 'message': 'App Running...' }

from app.db.base import Base
from app.db.session import engine

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)