from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 1️⃣ Custom State
class AgentState(TypedDict):
    question: str       # Current user question
    answer: str         # AI response
    model_name: str     # Model used

# 2️⃣ Models
basic_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_tokens=100,
    openai_api_key=api_key
)

advanced_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1,
    max_tokens=100,
    openai_api_key=api_key
)

#  Node function
def agent_node(state: AgentState) -> AgentState:
    # Prepare input
    user_message = [{"role": "user", "content": state["question"]}]
    print(state["question"])
    print(len(state["question"]))

    # Choose model
    if len(state["question"]) > 100:
        model = advanced_model
    else:
        model = basic_model
    print(model)
    # Correct property
    state["model_name"] = model.model_name
    print(state["model_name"])

    # Call model
    response = model.invoke(user_message)
    print(" ")
    # print(response)
   

    # Save AI output
    state["answer"] = response.content

    return state

#  Build Graph
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)
app = graph.compile()

# 5️⃣ Run
input_state = {
    "question": "What is AI?",
    "answer": "",
    "model_name": ""
}

result = app.invoke(input_state)

# print("Model used:", result["model_name"])
# print("Answer:", result["answer"])
