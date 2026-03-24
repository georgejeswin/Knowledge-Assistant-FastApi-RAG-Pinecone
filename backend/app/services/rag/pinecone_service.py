import pinecone
from app.core.config import settings

pinecone.init(api_key = settings.PINECONE_API_KEY)
index = pinecone.Index("rag-index")

class PineconeService:
    @staticmethod
    async def upsert(vectors):
        index.upsert(vectors=vectors)

    @staticmethod
    async def query(vector, top_k=5):
        return index.query(vector = vector, top_k=top_k, include_metadata=True)