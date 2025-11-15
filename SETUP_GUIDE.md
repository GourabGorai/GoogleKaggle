# Setup Guide

## 🔐 API Key Configuration (Required)

The community agents require a Google API key to function. Follow these steps:

### Step 1: Get Your API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Step 2: Configure Root .env File

1. Copy the example file:
   ```bash
   copy .env.example .env
   ```
   
2. Open `.env` and replace `your_api_key_here` with your actual API key:
   ```
   GOOGLE_API_KEY=AIzaSyC...your_actual_key_here
   ```

### Step 3: Configure Agent .env Files

Each agent needs its own `.env` file. Create them with your API key:

```bash
# For each agent directory, create a .env file
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/mental-health-support/.env
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/food-security-helper/.env
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/education-equity-guide/.env
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/climate-action-helper/.env
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/accessibility-advocate/.env
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/civic-engagement-guide/.env
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/research-agent/.env
echo GOOGLE_API_KEY=AIzaSyC...your_actual_key_here > agents/sample-agent/.env
```

**Or use this PowerShell script (Windows):**
```powershell
$apiKey = "AIzaSyC...your_actual_key_here"
"GOOGLE_API_KEY=$apiKey" | Out-File -FilePath .env -Encoding utf8
Get-ChildItem agents -Directory | ForEach-Object {
    "GOOGLE_API_KEY=$apiKey" | Out-File -FilePath "$($_.FullName)\.env" -Encoding utf8
}
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Test the Setup

```bash
# Test with CLI
python -m google.adk.cli run agents/mental-health-support

# Or start the web UI
python -m google.adk.cli web agents --port 8080
```

---

## ⚠️ Security Notes

- **NEVER commit `.env` files to git** - they contain your API key
- The `.gitignore` file is configured to prevent this
- If you accidentally commit your API key:
  1. Immediately revoke it at [Google AI Studio](https://aistudio.google.com/app/apikey)
  2. Generate a new API key
  3. Update your `.env` files
  4. Remove the key from git history

---

## 🚀 Quick Start After Setup

Once configured, start using the agents:

```bash
# Web UI (recommended)
python -m google.adk.cli web agents --port 8080
# Open http://127.0.0.1:8080

# CLI mode
python -m google.adk.cli run agents/mental-health-support

# Test script
python test_community_agent.py
```

---

## 📚 Next Steps

- Read [COMMUNITY_AGENTS_QUICKSTART.md](COMMUNITY_AGENTS_QUICKSTART.md) for usage examples
- Check [COMMUNITY_AGENTS_OVERVIEW.md](COMMUNITY_AGENTS_OVERVIEW.md) for full documentation
- Explore individual agents in the `agents/` directory

---

## 🆘 Troubleshooting

### "API key not valid" error
- Check that your `.env` files contain the correct API key
- Verify the key works at [Google AI Studio](https://aistudio.google.com/app/apikey)
- Make sure there are no extra spaces or quotes around the key

### "Module not found" error
- Run `pip install -r requirements.txt`
- Make sure you're in the project root directory

### Browser won't load (SSL error)
- Use `http://` not `https://`
- Try port 8080: `http://127.0.0.1:8080`
- See [START_AGENTS_WEB.md](START_AGENTS_WEB.md) for browser fixes

---

**Ready to make a difference! 🌍✨**
