"""
ADK Agent - A simple AI agent using Google's Agent Development Kit
"""
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

# Load environment variables from .env file
load_dotenv()


def setup_api_key():
    """Setup Gemini API key from environment"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "🔑 GOOGLE_API_KEY not found. Please set it in your .env file or environment variables."
        )
    os.environ["GOOGLE_API_KEY"] = api_key
    print("✅ Gemini API key setup complete.")


def configure_retry_options():
    """Configure retry options for handling transient errors"""
    return types.HttpRetryOptions(
        attempts=5,  # Maximum retry attempts
        exp_base=7,  # Delay multiplier
        initial_delay=1,  # Initial delay before first retry (in seconds)
        http_status_codes=[429, 500, 503, 504]  # Retry on these HTTP errors
    )


def create_agent(retry_config):
    """Create and configure the root agent"""
    agent = Agent(
        name="helpful_assistant",
        model=Gemini(
            model="gemini-2.5-flash-lite",
            retry_options=retry_config
        ),
        description="A simple agent that can answer general questions.",
        instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
        tools=[google_search],
    )
    print("✅ Root Agent defined.")
    return agent


async def run_agent(agent, query):
    """Run the agent with a given query"""
    runner = InMemoryRunner(agent=agent)
    print("✅ Runner created.")
    
    response = await runner.run_debug(query)
    return response


async def main():
    """Main function to setup and run the ADK agent"""
    print("🤖 Starting ADK Agent Setup...\n")
    
    # Step 1: Setup API key
    setup_api_key()
    
    # Step 2: Configure retry options
    retry_config = configure_retry_options()
    print("✅ Retry options configured.")
    
    # Step 3: Create agent
    root_agent = create_agent(retry_config)
    
    # Step 4: Run agent with a query
    print("\n🔍 Running agent query...\n")
    query = "What is Agent Development Kit from Google? What languages is the SDK available in?"
    await run_agent(root_agent, query)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
