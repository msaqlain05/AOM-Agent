from fastapi import FastAPI
from routers.agents import router as agent_router

app = FastAPI(title="AOM-Agent API")

app.include_router(agent_router)
