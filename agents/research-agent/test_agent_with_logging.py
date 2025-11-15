"""
Test script for the Research Paper Finder agent with LoggingPlugin
This demonstrates comprehensive logging for debugging and observability
"""
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import LoggingPlugin
from agent import root_agent


async def main():
    """Run a test query with the research agent using LoggingPlugin"""
    
    # Create runner with LoggingPlugin for comprehensive logging
    runner = InMemoryRunner(
        agent=root_agent,
        plugins=[
            LoggingPlugin()  # Handles standard Observability logging across ALL agents
        ]
    )
    
    print("✅ Runner configured with LoggingPlugin")
    print("\n🚀 Running agent with LoggingPlugin...")
    print("📊 Watch the comprehensive logging output below:\n")
    print("=" * 80)
    
    query = "Find recent papers on quantum computing"
    print(f"\n🔍 Query: {query}\n")
    
    response = await runner.run_debug(query)
    
    print("\n" + "=" * 80)
    print("\n✅ Agent execution completed!")
    print("\n📝 What the LoggingPlugin shows:")
    print("   • User message received")
    print("   • Invocation starting/completing")
    print("   • Agent starting/completing")
    print("   • LLM requests and responses")
    print("   • Tool execution (starting/completing)")
    print("   • Token usage statistics")
    print("   • Event yielding")
    print("   • Function calls and responses")
    

if __name__ == "__main__":
    asyncio.run(main())
