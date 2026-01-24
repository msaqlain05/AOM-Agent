from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlalchemy import text
from routers.agents import router as agent_router
from db.db import engine, Base
import model.chat  # Import all models here

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    print("🚀 Starting up AOM-Agent API...")
    
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database tables created/verified")
    
    # Test DB connection
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("✅ Database connected successfully")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down AOM-Agent API...")
    await engine.dispose()
    print("✅ Database connections closed")

# Initialize FastAPI app
app = FastAPI(
    title="AOM-Agent API",
    description="AI Agent API with streaming chat capabilities",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(agent_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to AOM-Agent API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}