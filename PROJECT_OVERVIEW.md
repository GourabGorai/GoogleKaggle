# ADK Agent Project - Complete Overview

## 🎯 Project Purpose

Build and debug AI agents using Google's Agent Development Kit (ADK) with hands-on learning exercises.

---

## 📁 Complete File Structure

```
project-root/
│
├── 📄 .env                                    # Root API key
├── 📄 requirements.txt                        # Dependencies
├── 📄 adk_agent.py                            # Standalone agent script
│
├── 📚 Documentation
│   ├── README.md                              # Main documentation
│   ├── PROJECT_STRUCTURE_AND_API_USAGE.md     # Complete analysis
│   ├── RESEARCH_AGENT_GUIDE.md                # Research agent guide
│   ├── IMPLEMENTATION_SUMMARY.md              # Implementation details
│   ├── QUICK_COMMANDS.md                      # Command reference
│   └── PROJECT_OVERVIEW.md                    # This file
│
├── 🤖 agents/                                 # ADK agents directory
│   │
│   ├── sample-agent/                          # Simple assistant
│   │   ├── agent.py                           # Agent definition
│   │   ├── test_agent.py                      # Test script
│   │   ├── __init__.py                        # Package init
│   │   └── .env                               # API key
│   │
│   └── research-agent/                        # Research paper finder
│       ├── agent.py                           # Multi-agent (with bug)
│       ├── test_agent.py                      # Test script
│       ├── __init__.py                        # Package init
│       ├── .env                               # API key
│       ├── README.md                          # Agent docs
│       └── FIX_THE_BUG.md                     # Fix guide
│
└── sample-agent/                              # Original agent (duplicate)
    ├── agent.py
    ├── test_agent.py
    ├── __init__.py
    └── .env
```

---

## 🤖 Agents Overview

### 1️⃣ Sample Agent (Helpful Assistant)

**Purpose:** General Q&A and information retrieval

**Architecture:**
```
User Query
    ↓
sample_agent
    ↓
google_search (if needed)
    ↓
Response
```

**Features:**
- Single agent system
- Google Search integration
- General purpose assistant

**Location:** `agents/sample-agent/`

---

### 2️⃣ Research Agent (Paper Finder) 🆕

**Purpose:** Find and count academic research papers (with intentional bug for learning)

**Architecture:**
```
User Query
    ↓
root_agent (research_paper_finder_agent)
    ↓
    ├─→ google_search_agent
    │       └─→ google_search tool
    │       └─→ Returns papers
    │
    └─→ count_papers tool
            └─→ 🐞 BUG: Counts characters instead of papers!
```

**Features:**
- Multi-agent system
- Agent delegation (root → search agent)
- Custom tool integration
- Intentional bug for debugging practice

**The Bug:**
```python
# Wrong (current):
def count_papers(papers: str):  # ❌ Should be List[str]
    return len(papers)  # Counts characters!
```

**Location:** `agents/research-agent/`

---

## 🔄 How to Run

### Method 1: Web UI (Recommended)
```bash
python -m google.adk.cli web agents --log_level DEBUG
```
- Visual interface at http://127.0.0.1:8000
- Events tab for execution traces
- Debug logs in terminal

### Method 2: Interactive CLI
```bash
python -m google.adk.cli run agents/research-agent
```
- Terminal-based chat
- Direct interaction

### Method 3: Test Scripts
```bash
python agents/research-agent/test_agent.py
```
- Automated testing
- Quick verification

### Method 4: Standalone Script
```bash
python adk_agent.py
```
- Single-file execution
- No agent directory needed

### Method 5: API Server
```bash
python -m google.adk.cli api_server agents
```
- HTTP API at http://127.0.0.1:8000
- Programmatic access

---

## 🔍 Debugging Features

### Events Tab (Web UI)
```
Timeline View:
├── call_llm (root_agent)
│   └── function_call: google_search_agent
│
├── execute_agent (google_search_agent)
│   └── call_llm
│       └── function_call: google_search
│
├── execute_tool (google_search)
│   └── returns: [papers list]
│
├── call_llm (root_agent)
│   └── function_call: count_papers
│       └── papers: "string..." ← 🐞 BUG HERE!
│
└── execute_tool (count_papers)
    └── returns: 5247 ← Wrong!
```

### Debug Logs (Terminal)
```
DEBUG: Full LLM prompt sent
DEBUG: Function call details
DEBUG: Tool execution
DEBUG: API responses
DEBUG: Internal state
```

---

## 📊 API Usage

### APIs Used
1. **Google Gemini API** - AI reasoning and responses
2. **Google Search API** - Real-time information retrieval

### API Flow
```
User Query
    ↓
Gemini API (analyze query)
    ↓
Gemini API (decide if search needed)
    ↓
Google Search API (if needed)
    ↓
Gemini API (process results)
    ↓
Response
```

### Configuration
```python
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504]
)
```

---

## 🎓 Learning Path

### Step 1: Run Sample Agent
```bash
python -m google.adk.cli web agents
# Select "sample-agent"
# Try: "What is ADK?"
```
**Learn:** Basic agent interaction

### Step 2: Run Research Agent (With Bug)
```bash
python -m google.adk.cli web agents --log_level DEBUG
# Select "research-agent"
# Try: "Find latest quantum computing papers"
```
**Learn:** Multi-agent systems, observe the bug

### Step 3: Debug Using Events Tab
```
1. Click "Events" tab
2. Find execute_tool count_papers
3. Click corresponding call_llm
4. Examine function_call
5. Notice papers is a string!
```
**Learn:** How to use Events tab for debugging

### Step 4: Read Debug Logs
```
Check terminal output:
- Full LLM prompts
- Function call details
- Tool execution logs
```
**Learn:** Understanding debug logs

### Step 5: Fix the Bug
```python
# Change line 17 in agents/research-agent/agent.py
def count_papers(papers: List[str]):  # Fixed!
```
**Learn:** How type annotations guide LLMs

### Step 6: Verify Fix
```bash
# Restart web UI
python -m google.adk.cli web agents --log_level DEBUG
# Test again - count should be ~10 now!
```
**Learn:** Testing and verification

---

## 🧪 Test Queries

### Sample Agent
```
✓ What is Agent Development Kit from Google?
✓ What are the latest features in Gemini 2.0?
✓ How do I build a multi-agent system with ADK?
✓ Explain how agents work
```

### Research Agent (Before Fix)
```
✓ Find latest quantum computing papers
  → Returns: ~5247 papers ❌ (counting characters)

✓ Search for machine learning research papers
  → Returns: ~6891 papers ❌ (counting characters)
```

### Research Agent (After Fix)
```
✓ Find latest quantum computing papers
  → Returns: ~10 papers ✅ (correct!)

✓ Search for machine learning research papers
  → Returns: ~12 papers ✅ (correct!)
```

---

## 📚 Documentation Guide

### For Getting Started
1. **README.md** - Start here for project overview
2. **QUICK_COMMANDS.md** - Command reference

### For Understanding the Project
1. **PROJECT_OVERVIEW.md** - This file (high-level view)
2. **PROJECT_STRUCTURE_AND_API_USAGE.md** - Detailed analysis

### For Research Agent
1. **RESEARCH_AGENT_GUIDE.md** - Quick start guide
2. **agents/research-agent/README.md** - Detailed docs
3. **agents/research-agent/FIX_THE_BUG.md** - How to fix

### For Implementation Details
1. **IMPLEMENTATION_SUMMARY.md** - What was built and why

---

## 🔧 Common Tasks

### Start Debugging Session
```bash
python -m google.adk.cli web agents --log_level DEBUG
```

### Test Agent Changes
```bash
# 1. Make changes to agent.py
# 2. Stop web UI (Ctrl+C)
# 3. Restart web UI
python -m google.adk.cli web agents
```

### View Agent Code
```bash
type agents\research-agent\agent.py
```

### Check API Key
```bash
type .env
```

---

## 🎯 Key Concepts

### Multi-Agent Systems
- **Root Agent**: Orchestrates workflow
- **Sub-Agents**: Specialized tasks
- **AgentTool**: Wraps agents as tools

### Tool Integration
- **Built-in Tools**: google_search
- **Custom Tools**: count_papers
- **Agent Tools**: Wrapped agents

### Type Annotations
```python
# LLMs use type hints to understand function signatures
def my_tool(data: List[str]):  # LLM passes a list
def my_tool(data: str):        # LLM passes a string
```

### Debugging
- **Events Tab**: Visual execution trace
- **Debug Logs**: Full LLM prompts and responses
- **Spans**: Individual execution steps

---

## 🚀 Next Steps

### After Mastering Basics
1. ✅ Fix the research agent bug
2. ✅ Add paper filtering by year
3. ✅ Create a summarization tool
4. ✅ Build a citation formatter
5. ✅ Add author search

### Advanced Topics
1. ✅ Multi-agent orchestration
2. ✅ Custom tool development
3. ✅ Error handling strategies
4. ✅ Performance optimization
5. ✅ Production deployment

---

## 📦 Dependencies

```
google-adk       # Agent Development Kit
python-dotenv    # Environment variables
```

**Install:**
```bash
pip install -r requirements.txt
```

---

## 🔐 Security Notes

⚠️ **API Key Exposed**: The `.env` files contain API keys
- Add `.env` to `.gitignore`
- Consider rotating the exposed key
- Never commit API keys to version control

---

## ✨ Project Highlights

✅ **Two Complete Agents**
- Sample agent (working)
- Research agent (with intentional bug)

✅ **Comprehensive Documentation**
- 7 documentation files
- Step-by-step guides
- Command references

✅ **Multiple Running Methods**
- Web UI (visual)
- CLI (interactive)
- Test scripts (automated)
- API server (programmatic)

✅ **Debugging Tools**
- Events tab
- Debug logs
- Execution traces

✅ **Learning-Focused**
- Intentional bug for practice
- Detailed fix guide
- Real-world examples

---

## 🎉 Summary

A complete ADK agent project with:
- ✅ Working sample agent
- ✅ Research agent with intentional bug
- ✅ Comprehensive documentation
- ✅ Multiple ways to run and test
- ✅ Debugging guides and tools
- ✅ Real-world learning exercises

**Ready to start debugging!** 🐞✨
