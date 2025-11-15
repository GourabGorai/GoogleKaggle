"""
Test script for the Research Paper Finder agent
"""
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from google.adk.runners import InMemoryRunner
from agent import root_agent


async def main():
    """Run a test query with the research agent"""
    runner = InMemoryRunner(agent=root_agent)
    
    query = "Find latest quantum computing papers"
    print(f"\n🔍 Testing research agent with query:\n{query}\n")
    
    response = await runner.run_debug(query)
    

if __name__ == "__main__":
    asyncio.run(main())
