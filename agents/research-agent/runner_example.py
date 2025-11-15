"""
Example of creating an InMemoryRunner with LoggingPlugin
This shows how to programmatically invoke the agent with comprehensive logging
"""
from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import LoggingPlugin
from google.genai import types
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the agent
from agent import root_agent


# Create the runner with LoggingPlugin
runner = InMemoryRunner(
    agent=root_agent,
    plugins=[
        LoggingPlugin()  # Handles standard Observability logging across ALL agents
    ]
)

print("✅ Runner configured with LoggingPlugin")
print("\n📊 LoggingPlugin provides:")
print("   • 🚀 USER MESSAGE RECEIVED - When user sends a message")
print("   • 🏃 INVOCATION STARTING - When agent invocation begins")
print("   • 🤖 AGENT STARTING - When specific agent starts")
print("   • 🧠 LLM REQUEST - LLM API calls with model, instructions, tools")
print("   • 🧠 LLM RESPONSE - LLM responses with content and token usage")
print("   • 📢 EVENT YIELDED - Events generated during execution")
print("   • 🔧 TOOL STARTING - When a tool begins execution")
print("   • 🔧 TOOL COMPLETED - When a tool finishes with results")
print("   • 🤖 AGENT COMPLETED - When agent finishes")
print("   • ✅ INVOCATION COMPLETED - When entire invocation completes")


async def run_with_logging(query: str):
    """
    Run the agent with comprehensive logging
    
    Args:
        query: The user's question or request
    """
    print(f"\n{'=' * 80}")
    print(f"🔍 Running query: {query}")
    print(f"{'=' * 80}\n")
    
    response = await runner.run_debug(query)
    
    print(f"\n{'=' * 80}")
    print("✅ Execution completed!")
    print(f"{'=' * 80}\n")
    
    return response


# Example usage
if __name__ == "__main__":
    # Run a test query
    asyncio.run(run_with_logging("Find recent papers on quantum computing"))
