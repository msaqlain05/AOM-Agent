from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessageChunk, BaseMessage
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# State
class AgentState(TypedDict):
    messages: List[BaseMessage]
    model_name: str



# Models (STREAMING ENABLED)

basic_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    streaming=True,
    openai_api_key=api_key
)

advanced_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1,
    streaming=True,
    openai_api_key=api_key
)



# Node

def agent_node(state: AgentState):
    user_message = state["messages"][-1].content

    model = advanced_model if len(user_message) > 100 else basic_model

    # STREAM TOKENS
    for chunk in model.stream(state["messages"]):
        yield {
            "messages": [AIMessageChunk(content=chunk.content)],
            "model_name": model.model_name,
        }



# Graph

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)
app = graph.compile()


# Run with Streaming


def Agent_chat_start(user_query):
    initial_state = {
        "messages": [HumanMessage(content=user_query)],
        "model_name": "",
    }

    for message, metadata in app.stream(
        initial_state,
        stream_mode="messages",
        config={"configurable": {"thread_id": "thread_1"}},
    ):
        if message.content:
            yield message.content

