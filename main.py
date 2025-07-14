# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from agent import run_agent

app = FastAPI(
    title="Agentic AI API",
    version="0.1.0",
    description="API to query an agent with PDF + web search and LangSmith tracing."
)

# Define the input model
class Query(BaseModel):
    question: str

# Root route (optional, for friendliness)
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <h2>👋 Welcome to Agentic AI FastAPI Server</h2>
    <p>Use the <a href='/docs'>interactive Swagger docs</a> to test the agent.</p>
    """

# POST endpoint for the agent
@app.post("/ask", summary="Ask Question")
def ask_question(query: Query):
    response = run_agent(query.question)
    return {"response": response}

