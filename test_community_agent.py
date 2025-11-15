"""
Quick test script for community agents
"""
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import required modules
import sys
sys.path.insert(0, 'agents/mental-health-support')
from agent import root_agent
from google.adk.runners import InMemoryRunner


async def test_agent():
    """Test the mental health support agent"""
    runner = InMemoryRunner(agent=root_agent)
    
    print("=" * 70)
    print("Testing Mental Health Support Agent")
    print("=" * 70)
    print()
    
    query = "What are some evidence-based coping strategies for anxiety?"
    print(f"Query: {query}")
    print()
    print("Response:")
    print("-" * 70)
    
    response = await runner.run_debug(query)
    
    print()
    print("=" * 70)
    print("Test completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(test_agent())
