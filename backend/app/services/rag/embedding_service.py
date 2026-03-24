from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key = settings.OPENAI_API_KEY)

class EmbeddingService:
    @staticmethod
    async def get_embeddings(texts: list[str]):
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )

        return [item.embedding for item in response.data]