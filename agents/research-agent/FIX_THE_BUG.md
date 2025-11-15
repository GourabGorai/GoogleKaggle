# 🔧 How to Fix the Research Agent Bug

## The Problem

The `count_papers` function has an incorrect type annotation that causes it to count characters instead of papers.

## Current Code (Broken)

```python
# Line 17 in agent.py
def count_papers(papers: str):
    """
    This function counts the number of papers in a list of strings.
    Args:
      papers: A list of strings, where each string is a research paper.
    Returns:
      The number of papers in the list.
    """
    return len(papers)
```

**What happens:**
- The LLM sees `papers: str` and passes a concatenated string
- `len(papers)` counts characters in the string
- Result: ~5000+ instead of ~10 papers

## The Fix

Change line 17 from:
```python
def count_papers(papers: str):
```

To:
```python
def count_papers(papers: List[str]):
```

## Complete Fixed Function

```python
def count_papers(papers: List[str]):
    """
    This function counts the number of papers in a list of strings.
    Args:
      papers: A list of strings, where each string is a research paper.
    Returns:
      The number of papers in the list.
    """
    return len(papers)
```

## Why This Works

1. **Type annotations guide the LLM**: When the function signature says `papers: List[str]`, the LLM knows to pass a list
2. **Proper data structure**: `len()` on a list counts items, not characters
3. **Correct semantics**: The function now matches its documentation

## How to Apply the Fix

### Option 1: Manual Edit
1. Open `agents/research-agent/agent.py`
2. Go to line 17
3. Change `papers: str` to `papers: List[str]`
4. Save the file

### Option 2: Using strReplace (if you're using Kiro)
```python
strReplace(
    path="agents/research-agent/agent.py",
    oldStr="def count_papers(papers: str):",
    newStr="def count_papers(papers: List[str]):"
)
```

## Verify the Fix

### Step 1: Restart the Web UI
```bash
# Stop the current server (Ctrl+C)
# Start it again
python -m google.adk.cli web agents --log_level DEBUG
```

### Step 2: Test Again
1. Open http://127.0.0.1:8000
2. Select "research-agent"
3. Type: "Find latest quantum computing papers"
4. Check the count - should be ~10-20 now!

### Step 3: Check the Events Tab
1. Click "Events" in the sidebar
2. Find the `execute_tool count_papers` event
3. Verify the input is now a list: `["paper1", "paper2", ...]`
4. Verify the output is a small number: `10`

## Before vs After

### Before Fix:
```
Query: "Find latest quantum computing papers"

Events Tab:
  call_llm → function_call
    papers: "Paper 1: Title...\nPaper 2: Title...\n..."  ← String!
  
  execute_tool count_papers
    input: "Paper 1: Title...\nPaper 2: Title...\n..."
    output: 5247  ← Counting characters!

Response: "I found 5247 papers"  ❌
```

### After Fix:
```
Query: "Find latest quantum computing papers"

Events Tab:
  call_llm → function_call
    papers: ["Paper 1: Title...", "Paper 2: Title...", ...]  ← List!
  
  execute_tool count_papers
    input: ["Paper 1: Title...", "Paper 2: Title...", ...]
    output: 10  ← Counting items!

Response: "I found 10 papers"  ✅
```

## Key Takeaways

1. **Type annotations are not just for Python** - LLMs use them to understand how to call functions
2. **Always match types to intent** - If you want a list, declare it as `List[str]`
3. **Debug with Events tab** - It shows exactly what data is passed between components
4. **Test after changes** - Always verify your fix works as expected

## Common Mistakes to Avoid

❌ **Don't do this:**
```python
def count_papers(papers):  # No type annotation
def count_papers(papers: Any):  # Too vague
def count_papers(papers: str):  # Wrong type (the bug!)
```

✅ **Do this:**
```python
def count_papers(papers: List[str]):  # Clear and correct
```

## Next Steps

After fixing this bug, try:
1. Add more validation (check if list is empty)
2. Add a tool to filter papers by year
3. Create a summarization tool
4. Build a citation formatter

Happy debugging! 🎉
