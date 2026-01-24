from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AgentRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User's message")
    sender: str = Field(..., min_length=1, description="Sender identifier")

class ChatResponse(BaseModel):
    id: int
    sender: str
    user_message: str
    bot_message: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # For Pydantic v2 (was orm_mode in v1)