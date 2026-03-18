from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(title = 'Knowledge Assistant')

app.include_router(api_router, prefix='/api/v1')

@app.get('/')
async def root():
    return { 'message': 'App Running...' }