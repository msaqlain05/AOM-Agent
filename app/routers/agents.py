from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from schemas.agents import AgentRequest
from controllers.agent_controller import chat_controller

router = APIRouter(prefix="/agent", tags=["Agent"])

@router.post("/chat")
async def chat(request: AgentRequest):
    try:
        generator = chat_controller(request)

        return StreamingResponse(
            generator,
            media_type="text/plain",
            headers={
                "Cache-Control": "no-cache",
                "X-Accel-Buffering": "no",  # IMPORTANT for nginx
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
