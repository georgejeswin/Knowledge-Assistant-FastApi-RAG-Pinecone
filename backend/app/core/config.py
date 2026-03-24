from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Knowledge Assistant(AI,RAG)"
    DATABASE_URL: str
    SECRET_KEY: str
    OPENAI_API_KEY: str
    PINECONE_API_KEY: str
    PINECONE_ENV: str

    class Config:
        env_file = ".env"


settings = Settings()