# Quick Command Reference

## 🚀 Running Agents

### Start Web UI (All Agents)
```bash
python -m google.adk.cli web agents
```

### Start Web UI with Debug Logs
```bash
python -m google.adk.cli web agents --log_level DEBUG
```

### Run Specific Agent (Interactive CLI)
```bash
# Sample agent
python -m google.adk.cli run agents/sample-agent

# Research agent
python -m google.adk.cli run agents/research-agent
```

### Run Test Scripts
```bash
# Sample agent
python sample-agent/test_agent.py

# Research agent
python agents/research-agent/test_agent.py

# Research agent with LoggingPlugin (comprehensive logging)
python agents/research-agent/test_agent_with_logging.py

# Runner example with LoggingPlugin
python agents/research-agent/runner_example.py
```

### Run Standalone Script
```bash
python adk_agent.py
```

### Start API Server
```bash
python -m google.adk.cli api_server agents
```

---

## 🐞 Debugging Commands

### Web UI with Different Log Levels
```bash
# Debug (most verbose)
python -m google.adk.cli web agents --log_level DEBUG

# Info (default)
python -m google.adk.cli web agents --log_level INFO

# Warning only
python -m google.adk.cli web agents --log_level WARNING

# Errors only
python -m google.adk.cli web agents --log_level ERROR
```

### Run with Debug Output
```bash
python -m google.adk.cli run agents/research-agent --log_level DEBUG
```

---

## 📁 File Operations

### View Agent Files
```bash
# List all agents
dir agents

# View research agent files
dir agents\research-agent

# View sample agent files
dir agents\sample-agent
```

### Read Agent Code
```bash
# Research agent
type agents\research-agent\agent.py

# Sample agent
type agents\sample-agent\agent.py
```

---

## 🔧 Fixing the Research Agent Bug

### Quick Fix (Manual)
1. Open `agents/research-agent/agent.py`
2. Go to line 17
3. Change: `def count_papers(papers: str):`
4. To: `def count_papers(papers: List[str]):`
5. Save and restart the web UI

### Verify Fix
```bash
# Restart web UI
python -m google.adk.cli web agents --log_level DEBUG

# Test in browser at http://127.0.0.1:8000
# Select "research-agent"
# Query: "Find latest quantum computing papers"
# Count should now be ~10 instead of ~5000
```

---

## 📚 Documentation

### View Documentation
```bash
# Main README
type README.md

# Research agent guide
type RESEARCH_AGENT_GUIDE.md

# Project structure
type PROJECT_STRUCTURE_AND_API_USAGE.md

# Implementation summary
type IMPLEMENTATION_SUMMARY.md

# Fix guide
type agents\research-agent\FIX_THE_BUG.md
```

---

## 🧪 Test Queries

### Sample Agent Queries
```
What is Agent Development Kit from Google?
What are the latest features in Gemini 2.0?
How do I build a multi-agent system with ADK?
```

### Research Agent Queries
```
Find latest quantum computing papers
Search for machine learning research papers
Get recent papers on climate change
Find papers about neural networks
Show me AI research papers from 2024
```

---

## 🌐 URLs

### Web UI
```
http://127.0.0.1:8000
```

### API Server
```
http://127.0.0.1:8000
```

---

## 🔑 Environment Setup

### Check API Key
```bash
type .env
type agents\sample-agent\.env
type agents\research-agent\.env
```

### Set API Key (if needed)
```bash
set GOOGLE_API_KEY=your_api_key_here
```

---

## 📦 Dependencies

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Check Installed Packages
```bash
pip list | findstr google-adk
pip list | findstr python-dotenv
```

### Upgrade Dependencies
```bash
pip install --upgrade google-adk python-dotenv
```

---

## 🛑 Stop Running Processes

### Stop Web UI
```
Press Ctrl+C in the terminal where it's running
```

### Stop API Server
```
Press Ctrl+C in the terminal where it's running
```

---

## 💡 Pro Tips

### Quick Test Workflow
```bash
# 1. Start web UI with debug logs
python -m google.adk.cli web agents --log_level DEBUG

# 2. Open browser to http://127.0.0.1:8000

# 3. Select agent from dropdown

# 4. Test queries

# 5. Check Events tab for traces

# 6. Check terminal for debug logs
```

### Debugging Workflow
```bash
# 1. Run with DEBUG logs
python -m google.adk.cli web agents --log_level DEBUG

# 2. Reproduce the issue

# 3. Check Events tab
#    - Click on spans
#    - Examine function calls
#    - Check inputs/outputs

# 4. Check terminal logs
#    - Look for errors
#    - Check LLM prompts
#    - Verify tool calls

# 5. Fix the issue

# 6. Restart and test
```

---

## 🎯 Common Tasks

### Create New Agent
```bash
# Manual method (recommended for Windows)
mkdir agents\my-agent
# Then create: __init__.py, agent.py, test_agent.py, .env
```

### Test Agent Changes
```bash
# Stop current web UI (Ctrl+C)
# Make your changes
# Restart web UI
python -m google.adk.cli web agents --log_level DEBUG
```

### Compare Agents
```bash
# View both agent files side by side
type agents\sample-agent\agent.py
type agents\research-agent\agent.py
```

---

## 📊 Project Status

### Check File Structure
```bash
dir /s /b agents
```

### Count Lines of Code
```bash
# PowerShell
(Get-Content agents\research-agent\agent.py).Count
(Get-Content agents\sample-agent\agent.py).Count
```

---

## 🔗 Quick Links

- **Main Docs**: `README.md`
- **Research Guide**: `RESEARCH_AGENT_GUIDE.md`
- **Fix Guide**: `agents/research-agent/FIX_THE_BUG.md`
- **Project Analysis**: `PROJECT_STRUCTURE_AND_API_USAGE.md`
- **Implementation Summary**: `IMPLEMENTATION_SUMMARY.md`

---

## ⚡ One-Liners

```bash
# Start and test research agent
python -m google.adk.cli web agents --log_level DEBUG

# Quick test without UI
python agents\research-agent\test_agent.py

# View the bug
type agents\research-agent\agent.py | findstr "def count_papers"

# Check all agents
dir agents /b
```

---

Happy coding! 🚀
