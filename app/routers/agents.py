from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.responses import StreamingResponse
from db.db import get_db
from model.chat import Chat
from schemas.agents import AgentRequest, ChatResponse
from controllers.agent_controller import chat_controller
from typing import List

router = APIRouter(prefix="/agents", tags=["Agents"])

# ------------------------
# Get All Chats
# ------------------------
@router.get("/chats", response_model=List[ChatResponse])
async def get_chats(
    limit: int = 50,
    session: AsyncSession = Depends(get_db)
):
    """Get recent chat messages."""
    result = await session.execute(
        select(Chat)
        .order_by(Chat.created_at.desc())
        .limit(limit)
    )
    chats = result.scalars().all()
    return chats

# ------------------------
# Streaming Chat Endpoint
# ------------------------
@router.post("/chat")
async def chat_stream(
    request: AgentRequest,
    session: AsyncSession = Depends(get_db)
):
    """
    Stream AI response token by token and save to DB.
    """
    async def generate():
        async for token in chat_controller(request, session):
            yield token

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )