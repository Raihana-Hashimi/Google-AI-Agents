from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from retry_config import retry_config
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

root_agent = Agent(
    name="helpful_assistant",
    model=Gemini(
        model_name="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

runner = InMemoryRunner(agent=root_agent)

async def main():
    response = await runner.run_debug("What is the weather in Kabul?")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())