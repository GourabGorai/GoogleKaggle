# Community Agents - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure API Key
The agents are already configured with an API key in their `.env` files. If you need to use your own:

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Update the `.env` file in each agent folder:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

### Step 3: Launch the Agents
```bash
python -m google.adk.cli web agents
```

Open your browser to: **http://127.0.0.1:8000**

---

## 🌟 Try These Example Conversations

### Mental Health Support Agent
```
"I'm feeling anxious about work. What are some coping strategies?"
"Find mental health support groups in Seattle"
"What should I do if I'm having a mental health crisis?"
```

### Food Security Helper
```
"Find food banks near zip code 90210"
"How do I apply for SNAP benefits in California?"
"Budget-friendly meal ideas for $50/week"
"Community gardens in Portland, Oregon"
```

### Education Equity Guide
```
"Free online courses for learning Python"
"Scholarships for community college students"
"How to apply for financial aid?"
"Adult education programs in Chicago"
```

### Climate Action Helper
```
"How can I reduce my carbon footprint at home?"
"Climate action groups in Austin, Texas"
"Government rebates for electric vehicles"
"How to start composting in an apartment"
```

### Accessibility Advocate
```
"How do I make my website accessible?"
"Best practices for writing alt text"
"Free accessibility testing tools"
"WCAG 2.1 compliance checklist"
```

### Civic Engagement Guide
```
"How do I register to vote in New York?"
"Find my local representatives"
"Upcoming city council meetings in San Francisco"
"How to organize a neighborhood meeting"
```

---

## 💡 Tips for Best Results

1. **Be specific about location** - Many resources are location-based
   - Good: "Food banks in zip code 10001"
   - Better: "Food banks in Manhattan, New York"

2. **Ask follow-up questions** - The agents maintain conversation context
   - "Tell me more about that program"
   - "What are the eligibility requirements?"

3. **Request local resources** - Agents use Google Search for current info
   - "Find organizations near me"
   - "What's available in my area?"

4. **Ask for practical steps** - Get actionable guidance
   - "What should I do first?"
   - "Walk me through the process"

---

## 🎯 Which Agent Should I Use?

**Need emotional support or mental health resources?**
→ Mental Health Support Agent

**Looking for food assistance or nutrition help?**
→ Food Security Helper

**Want to learn something new or find scholarships?**
→ Education Equity Guide

**Ready to take climate action?**
→ Climate Action Helper

**Building accessible websites or apps?**
→ Accessibility Advocate

**Want to get involved in your community or vote?**
→ Civic Engagement Guide

---

## 🔧 Troubleshooting

### "Failed to load agents"
Make sure you're in the project root directory and run:
```bash
python -m google.adk.cli web agents
```

### "Missing API key" error
Check that each agent's `.env` file contains:
```
GOOGLE_API_KEY=your_api_key_here
```

### Agent not responding
- Check your internet connection (agents use Google Search)
- Try refreshing the browser
- Restart the web UI

---

## 📱 Using from Command Line

Prefer terminal? Run any agent directly:

```bash
# Interactive chat in terminal
python -m google.adk.cli run agents/mental-health-support

# With debug logs
python -m google.adk.cli run agents/food-security-helper --log_level DEBUG
```

---

## 🤝 Real-World Use Cases

### For Individuals
- Find local resources and support
- Learn new skills for free
- Take action on issues you care about
- Get involved in your community
- Make informed decisions

### For Organizations
- Connect clients with resources
- Provide 24/7 information access
- Reduce staff workload on common questions
- Improve service accessibility
- Reach more people in need

### For Educators
- Help students find scholarships
- Connect families with food assistance
- Teach civic engagement
- Promote digital accessibility
- Support student mental health

### For Developers
- Learn accessibility best practices
- Build more inclusive products
- Understand community needs
- Contribute to social good
- Test agent frameworks

---

## 🌍 Making an Impact

These agents are designed to:
- **Reduce barriers** to essential resources
- **Empower people** with knowledge and tools
- **Build connections** between people and services
- **Promote equity** and social justice
- **Scale support** beyond what humans alone can provide

---

## 📚 Learn More

- Full documentation: `agents/COMMUNITY_AGENTS_README.md`
- Project overview: `PROJECT_OVERVIEW.md`
- ADK documentation: https://github.com/google/adk

---

## ⚠️ Remember

- These agents provide **information and resources**, not professional services
- Always seek **professional help** for serious issues
- Agents are **tools to support**, not replace, human connection
- **Privacy matters** - don't share sensitive personal information
- **Verify information** - agents do their best but can make mistakes

---

**Ready to make a difference? Start the agents and begin exploring!**

```bash
python -m google.adk.cli web agents
```

🌟 Every conversation is a step toward a more informed, connected, and empowered community.
