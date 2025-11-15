# Research Paper Finder Agent - Debugging Exercise

## Overview
This agent is designed to find academic research papers on any topic and count them. However, it contains an **intentional bug** for debugging practice!

## The Bug 🐞
The `count_papers` function has an incorrect type annotation:
- **Current (Wrong):** `papers: str`
- **Should be:** `papers: List[str]`

This causes the agent to count characters in a string instead of counting papers in a list!

## Agent Architecture

```
User Query
    ↓
root_agent (research_paper_finder_agent)
    ↓
    ├─→ google_search_agent (finds papers)
    │       └─→ google_search tool
    │
    └─→ count_papers tool (counts results)
```

## How to Debug

### Method 1: ADK Web UI with Debug Logs (Recommended)

1. **Start the web UI with debug logging:**
   ```bash
   python -m google.adk.cli web agents --log_level DEBUG
   ```

2. **Open the UI:**
   - Navigate to http://127.0.0.1:8000
   - Select "research-agent" from the dropdown

3. **Test the agent:**
   - Type: "Find latest quantum computing papers"
   - Observe the response - the count will be unusually large!

4. **Inspect the Events tab:**
   - Click "Events" in the left sidebar
   - Find the `execute_tool count_papers` span
   - Click the corresponding `call_llm` span
   - Examine the `function_call` - notice papers is passed as `str` instead of `List[str]`

### Method 2: Command Line Test

```bash
python agents/research-agent/test_agent.py
```

### Method 3: Interactive CLI

```bash
python -m google.adk.cli run agents/research-agent
```

### Method 4: With LoggingPlugin (Comprehensive Logging)

```bash
python agents/research-agent/test_agent_with_logging.py
```

This provides detailed logging output including:
- User message received
- Invocation starting/completing
- Agent starting/completing
- LLM requests and responses with token usage
- Tool execution details
- Event yielding
- Function calls and responses

## Expected Behavior (With Bug)

When you ask: "Find latest quantum computing papers"

**What happens:**
1. ✅ google_search_agent finds papers successfully
2. ❌ count_papers receives a string (concatenated papers)
3. ❌ Returns character count instead of paper count
4. ❌ Result: ~5000+ instead of ~10 papers

## How to Fix

Change line 17 in `agent.py`:

```python
# Before (Wrong):
def count_papers(papers: str):

# After (Correct):
def count_papers(papers: List[str]):
```

## Debug Log Levels

- `DEBUG` - Full LLM prompts, API responses, internal state
- `INFO` - General information about agent execution
- `WARNING` - Warning messages
- `ERROR` - Error messages only

## Key Learning Points

1. **Type annotations matter** - They guide the LLM on how to call functions
2. **Events tab is powerful** - Shows complete execution trace
3. **Debug logs reveal everything** - Full prompts and responses
4. **Multi-agent systems** - Root agent delegates to specialized agents

## Tools & Plugins Used

### Tools
- **google_search** - Built-in ADK tool for web search
- **count_papers** - Custom Python function (with intentional bug)
- **AgentTool** - Wraps google_search_agent for delegation

### Plugins
- **LoggingPlugin** - Provides comprehensive observability logging
  - Tracks all agent invocations
  - Logs LLM requests/responses
  - Shows tool execution details
  - Reports token usage
  - Displays event flow

## Agent Instructions

The root_agent follows these steps:
1. Use google_search_agent to find papers
2. Pass results to count_papers tool
3. Return both list and count

## Testing Queries

Try these queries to test the agent:
- "Find latest quantum computing papers"
- "Search for machine learning research papers"
- "Get recent papers on climate change"
- "Find papers about neural networks"

## After Fixing

Once you fix the type annotation, the agent should:
- Return accurate paper counts (10-20 papers typically)
- Properly parse the list of papers
- Provide both the list and correct count
