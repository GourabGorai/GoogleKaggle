from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

# Configure retry options for handling transient errors
retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,  # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504]  # Retry on these HTTP errors
)

root_agent = Agent(
    model=Gemini(
        model='gemini-2.5-flash-lite',
        retry_options=retry_config
    ),
    name='helpful_assistant',
    description='A simple agent that can answer general questions.',
    instruction='You are a helpful assistant. Use Google Search for current info or if unsure.',
    tools=[google_search],
)
