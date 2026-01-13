from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Dict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# -----------------------------
# Custom Types
# -----------------------------
class AgentState(TypedDict):
    question: str       # Current user question
    answer: str         # AI response
    model_name: str     # Model used


class ToolCall(TypedDict):
    name: str
    arguments: Dict[str, str]


class LLMOutput(TypedDict):
    id: str
    answer: str
    tool_calls: List[ToolCall]


class Metadata(TypedDict):
    model_name: str
    finish_reason: str
    token_usage: Dict[str, int]
    request_id: str


# -----------------------------
# Models
# -----------------------------
basic_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_tokens=200,
    openai_api_key=api_key
)

advanced_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1,
    max_tokens=100,
    openai_api_key=api_key
)


# -----------------------------
# Helper
# -----------------------------
def handle_response(llm_output: LLMOutput, metadata: Metadata):
    return {
        "llm_output": llm_output,
        "metadata": metadata
    }


# -----------------------------
# Node Function
# -----------------------------
def agent_node(state: AgentState) -> AgentState:
    # Pick model based on question length
    model = advanced_model if len(state["question"]) > 100 else basic_model
    state["model_name"] = model.model_name

    # Call model
    raw_response = model.invoke(state["question"])

    # Access raw attributes safely
    content = getattr(raw_response, "content", "")
    response_id = getattr(raw_response, "id", "")
    finish_reason = getattr(raw_response, "finish_reason", "")
    token_usage = getattr(raw_response, "token_usage", {})

    # Extract tool calls (if any)
    additional = getattr(raw_response, "additional_kwargs", {})
    tool_calls = additional.get("tool_calls", [])

    # --- LLM Output ---
    llm_output: LLMOutput = {
        "id": response_id,
        "answer": content,
        "tool_calls": tool_calls
    }

    # --- Metadata ---
    metadata: Metadata = {
        "model_name": model.model_name,
        "finish_reason": finish_reason,
        "token_usage": token_usage,
        "request_id": response_id
    }

    # Full structured response
    full_response = handle_response(llm_output, metadata)
    print("Full Response:", full_response)

    # Save AI answer in state
    state["answer"] = llm_output["answer"]

    return state


# -----------------------------
# Build Graph
# -----------------------------
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)
app = graph.compile()


# -----------------------------
# Run
# -----------------------------
user_query = input("You: ")

input_state = {
    "question": user_query,
    "answer": "",
    "model_name": ""
}

result = app.invoke(input_state)
print("Answer:", result["answer"])
print("Model used:", result["model_name"])
