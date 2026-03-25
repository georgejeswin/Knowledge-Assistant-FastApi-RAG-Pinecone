from app.repositories.chat_repository import ChatRepository
from app.services.rag.rag_service import RagService


class ChatService:

    @staticmethod
    async def build_prompt(db, user, message: str):

        # 1️⃣ Get history
        history = await ChatRepository.get_recent(db, user.id)

        history_text = ""
        for msg in reversed(history):
            role = "User" if msg.role == "user" else "Assistant"
            history_text += f"{role}: {msg.content}\n"

        # 2️⃣ Get RAG context
        contexts = await RagService.query(message)

        # 3️⃣ Final prompt
        prompt = f"""
        You are an AI assistant.

        Conversation:
        {history_text}

        Context:
        {contexts}

        User: {message}
        """

        return prompt