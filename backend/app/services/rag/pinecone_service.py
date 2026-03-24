from pinecone import Pinecone, ServerlessSpec
from app.core.config import settings
pc = Pinecone(api_key=settings.PINECONE_API_KEY)

if "rag-index" not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name="rag-index",
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index("rag-index")

class PineconeService:
    @staticmethod
    async def upsert(vectors):
        index.upsert(vectors=vectors)

    @staticmethod
    async def query(vector, top_k=5):
        return index.query(vector = vector, top_k=top_k, include_metadata=True)