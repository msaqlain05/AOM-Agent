from schemas.agents import AgentRequest, AgentResponse
from agents.app import Agent_chat_start

def chat_controller(request: AgentRequest):

    return Agent_chat_start(request.message)
