from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    role: Mapped[str] = mapped_column()  # "user" or "assistant"
    content: Mapped[str] = mapped_column(Text)