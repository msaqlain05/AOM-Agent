from sqlalchemy.ext.asyncio import AsyncSession
from model.chat import Chat
from agents.app import Agent_chat_start
from typing import AsyncGenerator
from schemas.agents import AgentRequest

async def chat_controller(
    request: AgentRequest, 
    session: AsyncSession
) -> AsyncGenerator[str, None]:
    """
    Streams AI response while saving the conversation to the DB.
    """
    bot_reply = ""

    # Stream AI response - Agent_chat_start is a regular generator
    try:
        for token in Agent_chat_start(request.message):
            bot_reply += token
            yield token
            
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        yield error_msg
        bot_reply = error_msg

    # Save full chat in DB after streaming completes
    try:
        chat = Chat(
            sender=request.sender,
            user_message=request.message,
            bot_message=bot_reply
        )
        # session.add(chat)
        # await session.commit()
    except Exception as e:
        await session.rollback()
        print(f"Database error: {e}")