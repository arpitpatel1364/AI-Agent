import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent 

# Import tools from our tools.py
from tools import tools_list

load_dotenv()

# Define the Structured Output format
class ResponseModel(BaseModel):
    response: str = Field(description="The final direct answer to the user")
    topic: str = Field(description="The main subject of the query")
    summary: str = Field(description="A 2-sentence summary of the research")
    tools_used: list[str] = Field(description="List of tools utilized")

# Initialize Ollama (Llama 3.1 is the best for tool-calling)
llm = ChatOllama(model="llama3.1", temperature=0)

# Create the Agentic Loop
# In 2026: 'prompt' sets the system instructions, 'response_format' enforces JSON
agent_executor = create_react_agent(
    model=llm,
    tools=tools_list,
    prompt=(
        "You are a professional Research AI. "
        "Use 'search_web' for current events and 'search_wikipedia' for facts. "
        "Always structure your final answer according to the schema."
    ),
    response_format=ResponseModel
)

def run_agent(user_input: str):
    print(f"\n--- Processing: {user_input} ---")
    
    # Send query as a message list
    inputs = {"messages": [("user", user_input)]}
    
    try:
        # The agent will now think, call tools, and return a result
        result = agent_executor.invoke(inputs)
        
        # Access the Pydantic-validated data
        data = result["structured_response"]
        
        print("\n[RESULT FOUND]")
        print(f"Topic:   {data.topic}")
        print(f"Summary: {data.summary}")
        print(f"Answer:  {data.response}")
        print(f"Tools:   {data.tools_used}")
        
    except Exception as e:
        print(f"Error: {e}. Make sure 'ollama serve' is running!")

if __name__ == "__main__":
    # Test query
    run_agent("what is the name of the capital of india?")