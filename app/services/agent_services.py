from schemas.agent import AgentRequest, AgentResponse

def get_agent_response(request: AgentRequest) -> AgentResponse:
    prompt = request.prompt
    # Example AI logic
    if "hello" in prompt.lower():
        reply = "Hello! How can I help you today?"
    elif "bye" in prompt.lower():
        reply = "Goodbye!"
    else:
        reply = f"AI received: '{prompt}'"

    return AgentResponse(prompt=prompt, response=reply)
