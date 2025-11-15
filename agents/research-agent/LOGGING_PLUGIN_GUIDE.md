# LoggingPlugin Guide - Comprehensive Observability

## 🎯 What is LoggingPlugin?

LoggingPlugin is a built-in ADK plugin that provides comprehensive observability logging across **all agents** in your multi-agent system. It tracks every step of agent execution, from user input to final response.

## 🚀 Quick Start

### Basic Usage

```python
from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import LoggingPlugin
from agent import root_agent

# Create runner with LoggingPlugin
runner = InMemoryRunner(
    agent=root_agent,
    plugins=[
        LoggingPlugin()  # That's it!
    ]
)

# Run your agent - logging happens automatically
response = await runner.run_debug("Your query here")
```

### Run the Example

```bash
python agents/research-agent/test_agent_with_logging.py
```

---

## 📊 What LoggingPlugin Logs

### 1. 🚀 USER MESSAGE RECEIVED
Logged when a user sends a message to the agent.

**Information:**
- Invocation ID (unique identifier)
- Session ID
- User ID
- App Name
- Root Agent name
- User content (the actual message)

**Example:**
```
[logging_plugin] 🚀 USER MESSAGE RECEIVED
[logging_plugin]    Invocation ID: e-c8943591-6d63-4a49-8e91-3a56ca8764ea
[logging_plugin]    Session ID: debug_session_id
[logging_plugin]    User ID: debug_user_id
[logging_plugin]    App Name: InMemoryRunner
[logging_plugin]    Root Agent: research_paper_finder_agent
[logging_plugin]    User Content: text: 'Find recent papers on quantum computing'
```

---

### 2. 🏃 INVOCATION STARTING
Logged when an agent invocation begins.

**Information:**
- Invocation ID
- Starting agent name

**Example:**
```
[logging_plugin] 🏃 INVOCATION STARTING
[logging_plugin]    Invocation ID: e-c8943591-6d63-4a49-8e91-3a56ca8764ea
[logging_plugin]    Starting Agent: research_paper_finder_agent
```

---

### 3. 🤖 AGENT STARTING
Logged when a specific agent starts execution.

**Information:**
- Agent name
- Invocation ID

**Example:**
```
[logging_plugin] 🤖 AGENT STARTING
[logging_plugin]    Agent Name: research_paper_finder_agent
[logging_plugin]    Invocation ID: e-c8943591-6d63-4a49-8e91-3a56ca8764ea
```

---

### 4. 🧠 LLM REQUEST
Logged when making a request to the LLM (Gemini).

**Information:**
- Model name
- Agent name
- System instruction (truncated)
- Available tools

**Example:**
```
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: research_paper_finder_agent
[logging_plugin]    System Instruction: 'Your task is to find research papers and count them...'
[logging_plugin]    Available Tools: ['google_search_agent', 'count_papers']
```

---

### 5. 🧠 LLM RESPONSE
Logged when receiving a response from the LLM.

**Information:**
- Agent name
- Content (text or function call)
- Token usage (input and output tokens)

**Example:**
```
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: research_paper_finder_agent
[logging_plugin]    Content: function_call: google_search_agent
[logging_plugin]    Token Usage - Input: 242, Output: 21
```

---

### 6. 📢 EVENT YIELDED
Logged when an event is generated during execution.

**Information:**
- Event ID
- Author (agent name)
- Content (text or function call/response)
- Final response flag
- Function calls/responses (if applicable)

**Example:**
```
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 2e6acd5a-f3d0-4a69-83e8-7903633e750c
[logging_plugin]    Author: research_paper_finder_agent
[logging_plugin]    Content: function_call: google_search_agent
[logging_plugin]    Final Response: False
[logging_plugin]    Function Calls: ['google_search_agent']
```

---

### 7. 🔧 TOOL STARTING
Logged when a tool begins execution.

**Information:**
- Tool name
- Agent name
- Function call ID
- Arguments passed to the tool

**Example:**
```
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: google_search_agent
[logging_plugin]    Agent: research_paper_finder_agent
[logging_plugin]    Function Call ID: adk-c7e83818-7d0a-4eb3-824a-a2edceb661eb
[logging_plugin]    Arguments: {'request': 'recent papers on quantum computing'}
```

---

### 8. 🔧 TOOL COMPLETED
Logged when a tool finishes execution.

**Information:**
- Tool name
- Agent name
- Function call ID
- Result (return value)

**Example:**
```
[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: count_papers
[logging_plugin]    Agent: research_paper_finder_agent
[logging_plugin]    Function Call ID: adk-58482ea8-878e-443d-83de-927a89aea240
[logging_plugin]    Result: 1
```

---

### 9. 🤖 AGENT COMPLETED
Logged when an agent finishes execution.

**Information:**
- Agent name
- Invocation ID

**Example:**
```
[logging_plugin] 🤖 AGENT COMPLETED
[logging_plugin]    Agent Name: research_paper_finder_agent
[logging_plugin]    Invocation ID: e-c8943591-6d63-4a49-8e91-3a56ca8764ea
```

---

### 10. ✅ INVOCATION COMPLETED
Logged when the entire invocation completes.

**Information:**
- Invocation ID
- Final agent name

**Example:**
```
[logging_plugin] ✅ INVOCATION COMPLETED
[logging_plugin]    Invocation ID: e-c8943591-6d63-4a49-8e91-3a56ca8764ea
[logging_plugin]    Final Agent: research_paper_finder_agent
```

---

## 🔍 Complete Execution Flow Example

Here's what you'll see for the research agent with the bug:

```
🚀 USER MESSAGE RECEIVED
   Query: "Find recent papers on quantum computing"

🏃 INVOCATION STARTING
   Agent: research_paper_finder_agent

🤖 AGENT STARTING
   Agent: research_paper_finder_agent

🧠 LLM REQUEST
   Model: gemini-2.5-flash-lite
   Tools: ['google_search_agent', 'count_papers']

🧠 LLM RESPONSE
   Content: function_call: google_search_agent
   Tokens: Input: 242, Output: 21

📢 EVENT YIELDED
   Function Calls: ['google_search_agent']

🔧 TOOL STARTING
   Tool: google_search_agent
   Arguments: {'request': 'recent papers on quantum computing'}

   🚀 USER MESSAGE RECEIVED (nested - google_search_agent)
   🏃 INVOCATION STARTING (google_search_agent)
   🤖 AGENT STARTING (google_search_agent)
   🧠 LLM REQUEST (google_search_agent)
   🧠 LLM RESPONSE (google_search_agent)
      Tokens: Input: 58, Output: 608
   📢 EVENT YIELDED (google_search_agent)
   🤖 AGENT COMPLETED (google_search_agent)
   ✅ INVOCATION COMPLETED (google_search_agent)

🔧 TOOL COMPLETED
   Tool: google_search_agent
   Result: [search results text]

📢 EVENT YIELDED
   Function Responses: ['google_search_agent']

🧠 LLM REQUEST
   (Processing search results)

🧠 LLM RESPONSE
   Content: function_call: count_papers
   Tokens: Input: 856, Output: 591

📢 EVENT YIELDED
   Function Calls: ['count_papers']

🔧 TOOL STARTING
   Tool: count_papers
   Arguments: {'papers': ["..."]}  ← Check this!

🔧 TOOL COMPLETED
   Tool: count_papers
   Result: 1  ← Bug visible here!

📢 EVENT YIELDED
   Function Responses: ['count_papers']

🧠 LLM REQUEST
   (Generating final response)

🧠 LLM RESPONSE
   Content: "I found 1 research paper..."
   Tokens: Input: 1462, Output: 61

📢 EVENT YIELDED
   Final Response: True

🤖 AGENT COMPLETED
   Agent: research_paper_finder_agent

✅ INVOCATION COMPLETED
```

---

## 🐞 Using LoggingPlugin for Debugging

### Finding the Bug

1. **Run with LoggingPlugin:**
   ```bash
   python agents/research-agent/test_agent_with_logging.py
   ```

2. **Look for TOOL STARTING (count_papers):**
   ```
   🔧 TOOL STARTING
      Tool Name: count_papers
      Arguments: {'papers': ["..."]}
   ```

3. **Check the Arguments:**
   - Is it a list? ✅
   - Is it a string? ❌ (Bug!)

4. **Look at TOOL COMPLETED:**
   ```
   🔧 TOOL COMPLETED
      Tool Name: count_papers
      Result: 5247  ← Way too high!
   ```

5. **Trace back to LLM RESPONSE:**
   - Check what the LLM decided to pass
   - Compare with function signature

---

## 💡 Benefits of LoggingPlugin

### 1. Complete Observability
- See every step of agent execution
- Track multi-agent interactions
- Monitor tool usage

### 2. Performance Monitoring
- Token usage per LLM call
- Total tokens for entire invocation
- Identify expensive operations

### 3. Debugging
- Trace execution flow
- Inspect function arguments
- Verify tool results
- Find where things go wrong

### 4. Multi-Agent Visibility
- See nested agent invocations
- Track delegation between agents
- Understand agent interactions

### 5. Production Monitoring
- Log all agent activities
- Track user interactions
- Monitor system health
- Analyze usage patterns

---

## 🎯 Use Cases

### Development
```python
# Use LoggingPlugin during development
runner = InMemoryRunner(
    agent=root_agent,
    plugins=[LoggingPlugin()]
)
```

### Testing
```python
# Verify agent behavior with detailed logs
response = await runner.run_debug("test query")
# Check logs for expected tool calls
```

### Debugging
```python
# Find issues by examining the complete execution trace
# Look for unexpected function calls or arguments
```

### Production Monitoring
```python
# Keep LoggingPlugin enabled in production
# Send logs to your monitoring system
# Track performance and usage
```

---

## 📊 Token Usage Tracking

LoggingPlugin shows token usage for every LLM call:

```
🧠 LLM RESPONSE
   Token Usage - Input: 242, Output: 21
```

**Calculate costs:**
- Input tokens: 242
- Output tokens: 21
- Total: 263 tokens per call

**For the research agent (with bug):**
- Initial call: 242 + 21 = 263 tokens
- Search agent: 58 + 608 = 666 tokens
- After search: 856 + 591 = 1,447 tokens
- Final response: 1,462 + 61 = 1,523 tokens
- **Total: ~3,899 tokens**

---

## 🔧 Advanced Usage

### Custom Logging

```python
from google.adk.plugins.logging_plugin import LoggingPlugin
import logging

# Configure Python logging
logging.basicConfig(level=logging.INFO)

# LoggingPlugin uses standard Python logging
runner = InMemoryRunner(
    agent=root_agent,
    plugins=[LoggingPlugin()]
)
```

### Multiple Plugins

```python
from google.adk.plugins.logging_plugin import LoggingPlugin
# Import other plugins as needed

runner = InMemoryRunner(
    agent=root_agent,
    plugins=[
        LoggingPlugin(),
        # Add other plugins here
    ]
)
```

---

## 📝 Summary

LoggingPlugin provides:
- ✅ Complete execution traces
- ✅ Token usage tracking
- ✅ Multi-agent visibility
- ✅ Tool execution details
- ✅ Event flow monitoring
- ✅ Debugging capabilities
- ✅ Production observability

**Use it for:**
- Development and debugging
- Performance monitoring
- Production observability
- Understanding agent behavior
- Tracking costs (token usage)

---

## 🚀 Next Steps

1. **Run the example:**
   ```bash
   python agents/research-agent/test_agent_with_logging.py
   ```

2. **Observe the logs** - See the complete execution flow

3. **Find the bug** - Look at the count_papers tool arguments

4. **Fix the bug** - Change `papers: str` to `papers: List[str]`

5. **Run again** - Verify the fix with LoggingPlugin

Happy logging! 📊✨
