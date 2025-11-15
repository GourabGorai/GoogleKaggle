# ADK Agent Project

AI agents built with Google's Agent Development Kit (ADK) following the official tutorial.

## Project Structure

```
.
├── agents/                      # ADK agents directory (for web UI)
│   ├── sample-agent/           # Simple helpful assistant
│   │   ├── agent.py            # Agent configuration with Google Search
│   │   ├── test_agent.py       # Test script
│   │   ├── .env                # API key configuration
│   │   └── __init__.py         # Package initialization
│   │
│   └── research-agent/         # Research Paper Finder (debugging exercise)
│       ├── agent.py            # Multi-agent with intentional bug
│       ├── test_agent.py       # Test script
│       ├── .env                # API key configuration
│       ├── __init__.py         # Package initialization
│       └── README.md           # Agent-specific documentation
│
├── sample-agent/               # Original agent (duplicate)
├── adk_agent.py                # Standalone agent implementation
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── PROJECT_STRUCTURE_AND_API_USAGE.md  # Complete project analysis
└── RESEARCH_AGENT_GUIDE.md     # Research agent quick start guide
```

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
- Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- The key is already configured in `.env` and `sample-agent/.env`
- Or set it as an environment variable:
  ```bash
  set GOOGLE_API_KEY=your_api_key_here
  ```

## Running the Agent

### Method 1: ADK Web UI (Recommended)
The web UI provides the best experience with visual traces of agent thoughts and actions.

```bash
python -m google.adk.cli web agents
```

Then open your browser to: **http://127.0.0.1:8000**

**Features:**
- Interactive chat interface
- Visual trace of agent reasoning
- See when and why the agent uses Google Search
- Step-by-step execution flow
- Session management

To stop the server: Press `Ctrl+C`

### Method 2: Command Line (Interactive)
Run the agent directly from the command line:

```bash
python -m google.adk.cli run agents/sample-agent
```

This starts an interactive session where you can chat with the agent in your terminal.

### Method 3: Python Script (Programmatic)
Run the standalone Python script:

```bash
python adk_agent.py
```

Or run the test script:

```bash
python sample-agent/test_agent.py
```

### Method 4: API Server
Start an API server to interact with the agent via HTTP:

```bash
python -m google.adk.cli api_server agents
```

The API will be available at: **http://127.0.0.1:8000**

You can then make POST requests to interact with the agent.

## Agents in This Project

### 1. Sample Agent (Helpful Assistant)
- **Model**: Gemini 2.5 Flash Lite
- **Tools**: Google Search for real-time information
- **Purpose**: General Q&A and information retrieval
- **Location**: `agents/sample-agent/`

### 2. Research Agent (Paper Finder) 🆕
- **Model**: Gemini 2.5 Flash Lite
- **Tools**: Google Search + Custom count_papers function
- **Plugins**: LoggingPlugin for comprehensive observability
- **Purpose**: Find and count academic research papers
- **Special**: Contains an intentional bug for debugging practice!
- **Location**: `agents/research-agent/`
- **Guides**: 
  - `RESEARCH_AGENT_GUIDE.md` - Quick start
  - `agents/research-agent/LOGGING_PLUGIN_GUIDE.md` - Observability guide

## Common Features

- **Retry Logic**: Automatic retry on rate limits and errors
- **Session Management**: Maintains conversation context
- **Multi-Agent Support**: Agents can delegate to other agents

## How It Works

The agent follows an agentic workflow:

1. **User Query** → Agent receives your question
2. **Reasoning** → Agent thinks about what information is needed
3. **Tool Use** → Agent decides to use Google Search if needed
4. **Observation** → Agent processes search results
5. **Response** → Agent provides an informed answer

This is different from a simple LLM - the agent can actively search for current information!

## Example Queries

### Sample Agent:
- "What is Agent Development Kit from Google? What languages is the SDK available in?"
- "What are the latest features in Gemini 2.0?"
- "How do I build a multi-agent system with ADK?"

### Research Agent:
- "Find latest quantum computing papers"
- "Search for machine learning research papers"
- "Get recent papers on climate change"
- Note: The count will be wrong due to the intentional bug! See `RESEARCH_AGENT_GUIDE.md` to learn how to debug it.

## Troubleshooting

### "Failed to load agents" in Web UI
Make sure you're running the web command with the `agents` directory:
```bash
python -m google.adk.cli web agents
```

### "Missing API key" error
Ensure your `.env` file contains:
```
GOOGLE_API_KEY=your_actual_api_key
```

### "adk command not found"
Use the full Python module syntax:
```bash
python -m google.adk.cli [command]
```

## 🐞 Debugging Exercise: Research Agent

The **research-agent** is a hands-on debugging exercise! It contains an intentional bug where the `count_papers` function has the wrong type annotation.

**Quick Start:**
```bash
# Start web UI with debug logs
python -m google.adk.cli web agents --log_level DEBUG

# Open http://127.0.0.1:8000
# Select "research-agent"
# Try: "Find latest quantum computing papers"
# Notice the count is way too high!
```

**Learn how to:**
- Use the Events tab to trace agent execution
- Read DEBUG logs to find bugs
- Understand how type annotations guide LLMs
- Debug multi-agent systems

**Full guide:** See `RESEARCH_AGENT_GUIDE.md` for step-by-step debugging instructions.

---

## Additional Resources

- [ADK Documentation](https://github.com/google/adk)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Docs](https://ai.google.dev/)
- `PROJECT_STRUCTURE_AND_API_USAGE.md` - Complete project analysis
- `RESEARCH_AGENT_GUIDE.md` - Research agent debugging guide
