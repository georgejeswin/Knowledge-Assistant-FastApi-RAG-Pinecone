import uuid
from app.services.rag.chunking import chunk_text
from app.services.rag.embedding_service import EmbeddingService
from app.services.rag.pinecone_service import PineconeService

class RagService:
    @staticmethod
    async def index_document(document):
        chunks = chunk_text(document.content)

        embeddings = await EmbeddingService.get_embeddings(chunks)

        vectors = []

        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            vectors.append({
                "id": str(uuid.uuid4()),
                "values": embedding,
                "metadata": {
                    "text": chunk,
                    "document_id": document.id
                }
            })

        await PineconeService.upsert(vectors)

    @staticmethod
    async def query(query_text: str):
        query_embeddings = await EmbeddingService.get_embeddings([query_text])
        results = await PineconeService.query(query_embeddings[0])

        contexts = [ match["metadata"]["texts"] for match in results["matches"]]

        return contexts