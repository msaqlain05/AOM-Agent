from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from db.db import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sender = Column(String(100), nullable=False, index=True)
    user_message = Column(Text, nullable=False)
    bot_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Chat(id={self.id}, sender={self.sender})>"