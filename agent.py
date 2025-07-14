# agent.py

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from tavily import TavilyClient

# Load environment variables
load_dotenv()
import langsmith 
from langsmith import traceable


# Configure LangSmith observability
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")  # already in .env


# Load vectorstore from local path
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("vectorstore", embedding_model, allow_dangerous_deserialization=True)

# Tavily client
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))




# Tavily Search Tool
def tavily_search(query: str) -> str:
    """Search the web using Tavily."""
    search_results = tavily.search(query=query, max_results=3)
    return "\n".join([result["content"] for result in search_results["results"]])

# PDF Retriever Tool
def pdf_retriever(query: str) -> str:
    """Search the local PDF knowledge base."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    return "\n".join([doc.page_content for doc in docs]) if docs else "No relevant information found."

# Tool List
tools = [
    Tool(name="PDF_Retriever", func=pdf_retriever, description="Searches local PDFs for answers."),
    Tool(name="Tavily_Search", func=tavily_search, description="Searches the web using Tavily.")
]

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intelligent assistant. Use PDF_Retriever first. If it's not helpful, use Tavily_Search."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# Load LLM and Agent
llm = ChatGroq(model="llama3-8b-8192", temperature=0,  api_key=os.getenv("GROQ_API_KEY"))
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Query Function
@traceable(name="run_agent")
def run_agent(query: str) -> str:
    response = agent_executor.invoke({"input": query})
    return response["output"]




if __name__ == "__main__":
    while True:
        user_input = input("Ask a question (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        response = run_agent(user_input)
        print("\n🧠 Agent Response:\n", response)

