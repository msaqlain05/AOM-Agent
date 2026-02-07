from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Literal
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessageChunk, BaseMessage, SystemMessage
from dotenv import load_dotenv
import os
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
import re

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# SQLite checkpointer
checkpointer = SqliteSaver(
    sqlite3.connect("checkpoint.db", check_same_thread=False)
)

# Enhanced State
class AgentState(TypedDict):
    messages: List[BaseMessage]
    model_name: str
    topic_category: str  # architecture, algorithms, design_patterns, etc.
    complexity_level: str  # beginner, intermediate, advanced
    include_code: bool
    user_profile: dict  # Track user's learning progress


# Advanced Models
basic_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    streaming=True,
    openai_api_key=api_key
)

advanced_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    streaming=True,
    openai_api_key=api_key
)

# System Prompt - Expert Software Engineering Tutor
SYSTEM_PROMPT = """You are an elite Software Engineering AI Tutor with deep expertise across:

**CORE DOMAINS:**
1. Software Architecture (Microservices, Event-Driven, Clean Architecture, DDD)
2. Design Patterns (GoF Patterns, Enterprise Patterns, Cloud Patterns)
3. Data Structures & Algorithms (Complexity Analysis, Optimization)
4. System Design (Scalability, Distributed Systems, CAP Theorem)
5. AI/ML Engineering (Model Training, MLOps, LLM Integration)
6. DevOps & Cloud (CI/CD, Kubernetes, Infrastructure as Code)
7. Best Practices (SOLID, DRY, Testing, Code Review)
8. Modern Frameworks (React, Django, FastAPI, LangGraph, etc.)

**TEACHING APPROACH:**
- Break down complex concepts into digestible parts
- Use real-world analogies and examples
- Provide production-ready code samples
- Include diagrams and visual explanations when helpful
- Cite industry best practices and trade-offs
- Adapt explanation depth to user's level
- Guide through problem-solving, don't just give answers
- Connect concepts to practical applications

**CODE EXAMPLES:**
- Always provide clean, well-commented code
- Include error handling and edge cases
- Show both simple and advanced implementations
- Explain time/space complexity
- Suggest optimizations and alternatives

Be encouraging, patient, and thorough. Build confidence while maintaining technical accuracy."""


# Router Node - Classify the query
def router_node(state: AgentState) -> AgentState:
    """Analyze user query to determine topic and complexity"""
    user_message = state["messages"][-1].content.lower()
    
    # Detect topic categories
    topic_keywords = {
        "architecture": ["architecture", "microservices", "monolith", "design system", "distributed"],
        "algorithms": ["algorithm", "complexity", "big o", "optimization", "data structure"],
        "design_patterns": ["pattern", "singleton", "factory", "observer", "mvc", "solid"],
        "system_design": ["system design", "scalability", "load balancing", "caching", "database design"],
        "ai_ml": ["machine learning", "ai", "neural network", "llm", "model", "training", "mlops"],
        "devops": ["devops", "ci/cd", "docker", "kubernetes", "deployment", "infrastructure"],
        "web_dev": ["web", "api", "rest", "graphql", "frontend", "backend", "react", "django"],
        "best_practices": ["best practice", "clean code", "testing", "refactor", "code review"]
    }
    
    detected_topic = "general"
    for topic, keywords in topic_keywords.items():
        if any(keyword in user_message for keyword in keywords):
            detected_topic = topic
            break
    
    # Detect complexity level
    complexity = "intermediate"
    if any(word in user_message for word in ["beginner", "basic", "introduction", "eli5", "simple"]):
        complexity = "beginner"
    elif any(word in user_message for word in ["advanced", "expert", "deep dive", "complex", "production"]):
        complexity = "advanced"
    
    # Check if code examples are needed
    include_code = any(word in user_message for word in 
                      ["code", "example", "implement", "show me", "how to", "build"])
    
    return {
        **state,
        "topic_category": detected_topic,
        "complexity_level": complexity,
        "include_code": include_code
    }


# Main Agent Node - Enhanced Teaching
def agent_node(state: AgentState):
    """Main teaching agent with context-aware responses"""
    
    # Build enhanced system message based on routing
    enhanced_prompt = f"""{SYSTEM_PROMPT}

**CURRENT CONTEXT:**
- Topic: {state['topic_category']}
- User Level: {state['complexity_level']}
- Code Examples: {'Required' if state['include_code'] else 'Optional'}

Tailor your response accordingly."""

    # Prepare messages with system prompt
    messages = [SystemMessage(content=enhanced_prompt)] + state["messages"]
    
    # Select model based on complexity and message length
    user_message = state["messages"][-1].content
    use_advanced = (
        len(user_message) > 100 or 
        state['complexity_level'] == 'advanced' or
        state['topic_category'] in ['system_design', 'ai_ml', 'architecture']
    )
    
    model = advanced_model if use_advanced else basic_model
    
    # Stream response
    for chunk in model.stream(messages):
        if chunk.content:
            yield {
                "messages": [AIMessageChunk(content=chunk.content)],
                "model_name": model.model_name,
            }


# Follow-up Suggestions Node
def suggest_followup(state: AgentState) -> AgentState:
    """Suggest related topics to explore"""
    
    suggestions = {
        "architecture": [
            "Would you like to explore microservices communication patterns?",
            "Interested in learning about Clean Architecture?",
            "Want to dive into Event-Driven Architecture?"
        ],
        "algorithms": [
            "Should we analyze the time complexity of different sorting algorithms?",
            "Want to practice implementing common data structures?",
            "Interested in dynamic programming techniques?"
        ],
        "design_patterns": [
            "Should we implement this pattern in a real-world scenario?",
            "Want to compare this with alternative patterns?",
            "Interested in when NOT to use this pattern?"
        ],
        "ai_ml": [
            "Would you like to build a complete ML pipeline?",
            "Interested in LangGraph for AI agent development?",
            "Want to explore MLOps best practices?"
        ]
    }
    
    topic = state.get('topic_category', 'general')
    if topic in suggestions:
        suggestion_msg = "\n\n💡 **Next Steps:**\n" + "\n".join(
            f"- {s}" for s in suggestions[topic][:2]
        )
        
        # Append suggestion to last message
        last_msg = state["messages"][-1]
        if hasattr(last_msg, 'content'):
            last_msg.content += suggestion_msg
    
    return state


# Build Graph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("router", router_node)
graph.add_node("agent", agent_node)
graph.add_node("followup", suggest_followup)

# Add edges
graph.add_edge(START, "router")
graph.add_edge("router", "agent")
graph.add_edge("agent", "followup")
graph.add_edge("followup", END)

# Compile
app = graph.compile(checkpointer=checkpointer)


# Enhanced Chat Interface
def software_engineering_tutor(user_query: str, thread_id: str = "thread_1"):
    """
    Main interface for the Software Engineering AI Tutor
    
    Args:
        user_query: User's question or topic
        thread_id: Conversation thread identifier
    
    Yields:
        Streamed response chunks
    """
    
    initial_state = {
        "messages": [HumanMessage(content=user_query)],
        "model_name": "",
        "topic_category": "",
        "complexity_level": "",
        "include_code": False,
        "user_profile": {}
    }

    print(f"🎓 Software Engineering AI Tutor\n{'='*50}")
    
    # Stream response
    for message, metadata in app.stream(
        initial_state,
        stream_mode="messages",
        config={"configurable": {"thread_id": thread_id}},
    ):
        if message.content:
            print(message.content, end="", flush=True)
            yield message.content

    # Get and display checkpoint state
    state = app.get_state(config={"configurable": {"thread_id": thread_id}})
    
    print("\n\n" + "="*50)
    print("📊 SESSION INFO")
    print("="*50)
    print(f"Thread ID: {thread_id}")
    print(f"Topic: {state.values.get('topic_category', 'N/A')}")
    print(f"Level: {state.values.get('complexity_level', 'N/A')}")
    print(f"Model: {state.values.get('model_name', 'N/A')}")
    print(f"Messages: {len(state.values.get('messages', []))}")
    print("="*50 + "\n")


# Utility: Continue conversation
def continue_conversation(thread_id: str = "thread_1"):
    """Continue an existing conversation"""
    
    while True:
        user_input = input("\n🤔 Your question (or 'exit' to quit): ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("👋 Happy coding! Keep building amazing software!")
            break
        
        if not user_input:
            continue
        
        # Get current state and add new message
        current_state = app.get_state(config={"configurable": {"thread_id": thread_id}})
        
        updated_state = {
            **current_state.values,
            "messages": current_state.values["messages"] + [HumanMessage(content=user_input)]
        }
        
        # Stream response
        for _ in software_engineering_tutor(user_input, thread_id):
            pass


# Example Usage
if __name__ == "__main__":
    # Example 1: System Design Question
    print("\n🚀 EXAMPLE 1: System Design\n")
    for _ in software_engineering_tutor(
        "Explain how to design a scalable URL shortener service like bit.ly. Include architecture and database design.",
        thread_id="demo_1"
    ):
        pass
    
    print("\n\n")
    
    # Example 2: AI/ML Engineering
    print("🚀 EXAMPLE 2: AI Engineering\n")
    for _ in software_engineering_tutor(
        "How do I build an AI agent using LangGraph? Show me code examples.",
        thread_id="demo_2"
    ):
        pass
    
    # Uncomment to start interactive mode:
    # continue_conversation("my_session")