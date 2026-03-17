import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent 

# Import tools from our tools.py
from tools import tools_list

load_dotenv()

# 1. Define the Structured Output format
class ResponseModel(BaseModel):
    response: str = Field(description="The final direct answer to the user")
    topic: str = Field(description="The main subject of the query")
    summary: str = Field(description="A 2-sentence summary of the research")
    tools_used: list[str] = Field(description="List of tools utilized")

# 2. Initialize LLM
llm = ChatOllama(model="llama3.1", temperature=0)

# 3. Create the Agent
agent_executor = create_react_agent(
    model=llm,
    tools=tools_list,
    prompt=(
        "You are a professional Research AI. "
        "Use 'search_web' for current events and 'search_wikipedia' for facts. "
        "Always structure your final answer according to the provided schema."
    ),
    response_format=ResponseModel
)

def start_chat():
    # This list will store the conversation history
    chat_history = []
    
    print("\n" + "="*50)
    print("🤖 AI Research Agent is Online (March 2026)")
    print("Type 'exit' or 'quit' to stop the conversation.")
    print("="*50 + "\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye! Have a great day.")
            break

        # Append the new user message to history
        chat_history.append(("user", user_input))
        
        print("\nAgent is thinking...")

        try:
            # We pass the entire chat_history to the agent
            inputs = {"messages": chat_history}
            result = agent_executor.invoke(inputs)
            
            # Access the Pydantic data
            data = result["structured_response"]
            
            # Print the structured result nicely
            print("\n" + "-"*30)
            print(f" TOPIC:   {data.topic}")
            print(f" SUMMARY: {data.summary}")
            print(f" ANSWER:  {data.response}")
            print(f" TOOLS:   {', '.join(data.tools_used) if data.tools_used else 'None'}")
            print("-"*30 + "\n")

            # Add the agent's response to history so it remembers for the next question
            chat_history.append(("assistant", data.response))

        except Exception as e:
            print(f"❌ Error: {e}")
            print("Hint: Ensure 'ollama serve' is running and you have pulled 'llama3.1'.")

if __name__ == "__main__":
    start_chat()