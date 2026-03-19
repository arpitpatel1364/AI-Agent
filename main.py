import asyncio
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

# Import tools from your tools.py
from tools import tools_list

load_dotenv()

# 1. Define the Structured Output format
class ResponseModel(BaseModel):
    response: str = Field(description="The final direct answer to the user")
    topic: str = Field(description="The main subject of the query")
    summary: str = Field(description="A 2-sentence summary of the research")
    tools_used: list[str] = Field(description="List of tools utilized")

# 2. Initialize LLM with Streaming enabled
llm = ChatOllama(model="llama3.1", temperature=0, streaming=True)

# 3. Create the Agent
agent_executor = create_react_agent(
    model=llm,
    tools=tools_list,
    prompt=(
        "You are a professional Research AI. "
        "Use 'search_web' for current events and 'search_wikipedia' for facts."
    ),
    response_format=ResponseModel
)

async def run_research_loop():
    chat_history = []
    
    print("\n" + "═"*50)
    print("RESEARCH AGENT (TERMINAL MODE)")
    print(" Type 'exit' to quit")
    print("═"*50 + "\n")

    while True:
        user_input = input("User 👤: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nExiting. Happy coding!")
            break

        chat_history.append(("user", user_input))
        print("\nAgent 🤖 thinking...", end="\r")

        try:
            # Using invoke for structured response
            # Note: For even faster "token-by-token" visual, 
            # you'd use astream_events, but invoke is safer for Pydantic.
            result = await agent_executor.ainvoke({"messages": chat_history})
            
            data = result["structured_response"]
            
            # Attractive Terminal Formatting
            print(f"\r{'─'*50}")
            print(f"📌 TOPIC:   {data.topic.upper()}")
            print(f"📝 SUMMARY: {data.summary}")
            print(f"✅ ANSWER:  {data.response}")
            print(f"🛠️  TOOLS:   {', '.join(data.tools_used) if data.tools_used else 'Internal Knowledge'}")
            print(f"{'─'*50}\n")

            chat_history.append(("assistant", data.response))

        except Exception as e:
            print(f"\n Error: {e}")

if __name__ == "__main__":
    # Standard way to run async code in modern Python
    asyncio.run(run_research_loop())