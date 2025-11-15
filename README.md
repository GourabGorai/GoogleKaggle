# AI Agents for Social Good 🌍

Community-focused AI agents built with Google's Agent Development Kit (ADK) to benefit larger communities and support important social causes.

## 🎯 Project Mission

Build AI agents that serve communities by providing 24/7 access to resources, information, and support for critical social needs. These agents connect people with local services, educational opportunities, mental health resources, and civic engagement tools.

---

## 🤖 Six Community-Focused Agents

### 1. 💚 Mental Health Support Agent
**Purpose:** Provide mental health resources, crisis support, and compassionate guidance

**Features:**
- Crisis hotlines (988, Crisis Text Line, international resources)
- Evidence-based coping strategies
- Local mental health services finder
- Support group connections
- Safety-first approach with professional referrals

**Example:** *"I'm feeling anxious. What resources are available?"*

---

### 2. 🍽️ Food Security Helper
**Purpose:** Connect people with food assistance and promote food security

**Features:**
- Food bank and pantry locator
- SNAP/WIC application guidance
- Budget meal planning
- Community garden connections
- Nutrition education

**Example:** *"Find food banks near zip code 90210"*

---

### 3. 📚 Education Equity Guide
**Purpose:** Make quality education accessible to everyone

**Features:**
- Free online learning platforms (Khan Academy, Coursera, etc.)
- Scholarship and financial aid finder
- Tutoring and mentorship programs
- Alternative education pathways
- Adult education resources

**Example:** *"Free online courses for learning Python"*

---

### 4. 🌱 Climate Action Helper
**Purpose:** Empower individuals and communities to take climate action

**Features:**
- Carbon footprint reduction tips
- Local climate groups and volunteer opportunities
- Sustainable living resources
- Government incentives (solar, EV rebates)
- Climate policy engagement

**Example:** *"How can I reduce my carbon footprint at home?"*

---

### 5. ♿ Accessibility Advocate
**Purpose:** Promote digital accessibility and inclusive design

**Features:**
- WCAG/ADA compliance guidance
- Assistive technology resources
- Accessibility testing tools
- Alt text and caption best practices
- Inclusive design principles

**Example:** *"How do I make my website WCAG compliant?"*

---

### 6. 🗳️ Civic Engagement Guide
**Purpose:** Help people participate in democracy and build communities

**Features:**
- Voter registration assistance
- Representative contact information
- Public meeting schedules
- Community organizing resources
- Government structure education

**Example:** *"How do I register to vote in New York?"*

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key (Required)
⚠️ **Important:** You need your own Google API key.

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Copy `.env.example` to `.env` and add your key
3. Create `.env` files in each agent directory

**See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions.**

### 3. Launch the Agents
```bash
# Web UI (recommended)
python -m google.adk.cli web agents --port 8080

# Open http://127.0.0.1:8080 in your browser
```

**Alternative: CLI Mode**
```bash
python -m google.adk.cli run agents/mental-health-support
```

---

## 📁 Project Structure

```
.
├── agents/                                    # Community-focused agents
│   ├── mental-health-support/                # Crisis resources & support
│   ├── food-security-helper/                 # Food assistance & nutrition
│   ├── education-equity-guide/               # Free learning & scholarships
│   ├── climate-action-helper/                # Environmental action
│   ├── accessibility-advocate/               # Digital inclusion
│   ├── civic-engagement-guide/               # Democracy & organizing
│   ├── research-agent/                       # Academic paper finder (with bug)
│   └── sample-agent/                         # Simple helpful assistant
│
├── 📚 Documentation
│   ├── README.md                             # This file
│   ├── SETUP_GUIDE.md                        # Detailed setup instructions
│   ├── COMMUNITY_AGENTS_QUICKSTART.md        # Quick start with examples
│   ├── COMMUNITY_AGENTS_OVERVIEW.md          # Complete overview
│   ├── COMMUNITY_AGENTS_SUMMARY.md           # Impact & vision
│   ├── PROJECT_OVERVIEW.md                   # Technical details
│   └── SECURITY_NOTICE.md                    # Important security info
│
├── .env.example                              # API key template
├── .gitignore                                # Prevents committing secrets
├── requirements.txt                          # Python dependencies
└── test_community_agent.py                   # Test script
```

---

## 💡 Example Use Cases

### For Individuals
- Find local resources and support services
- Learn new skills for free
- Take action on issues you care about
- Get involved in your community
- Make informed decisions

### For Organizations
- Embed agents on websites for 24/7 information
- Reduce staff workload on common questions
- Improve service accessibility
- Reach more people in need
- Scale support beyond human capacity

### For Developers
- Learn to build socially-conscious AI
- Practice agent development with ADK
- Understand community needs
- Implement safety protocols
- Contribute to social good

---

## 🎯 Key Features

### For Users
✅ 24/7 availability  
✅ No judgment or stigma  
✅ Local, current resources via Google Search  
✅ Actionable, practical guidance  
✅ Free and accessible  
✅ Privacy-respecting  

### For Developers
✅ Built with Google ADK  
✅ Easy to customize and extend  
✅ Well-documented code  
✅ Safety protocols included  
✅ Accessibility-focused design  
✅ Open for contributions  

---

## 🔒 Safety & Ethics

### Built-in Safeguards
- Mental health agent prioritizes crisis resources
- All agents direct to professional help when needed
- Non-judgmental, dignity-preserving language
- Evidence-based information
- Clear disclaimers about limitations
- Privacy-respecting (no data storage)

### What These Agents Are NOT
- ❌ Not professional therapists, doctors, or lawyers
- ❌ Not direct service providers
- ❌ Not emergency services
- ❌ Not guaranteed to be 100% accurate
- ❌ Not a substitute for human connection

---

## 📖 Documentation

### Getting Started
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions
- **[COMMUNITY_AGENTS_QUICKSTART.md](COMMUNITY_AGENTS_QUICKSTART.md)** - Quick start with 30+ example queries

### Full Documentation
- **[COMMUNITY_AGENTS_OVERVIEW.md](COMMUNITY_AGENTS_OVERVIEW.md)** - Complete overview & poster prompt
- **[COMMUNITY_AGENTS_SUMMARY.md](agents/COMMUNITY_AGENTS_SUMMARY.md)** - Impact, metrics, and future vision
- **[agents/COMMUNITY_AGENTS_README.md](agents/COMMUNITY_AGENTS_README.md)** - Detailed agent documentation

### Technical Details
- **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - Complete technical overview
- **[SECURITY_NOTICE.md](SECURITY_NOTICE.md)** - Important security information

---

## 🛠️ Technical Stack

- **Framework:** Google Agent Development Kit (ADK)
- **Model:** Gemini 2.5 Flash Lite
- **Tools:** Google Search for real-time information
- **Language:** Python 3.13+
- **Features:** Retry logic, session management, multi-agent support

---

## 🌟 Design Principles

1. **Equity** - Everyone deserves access to resources
2. **Dignity** - Respectful, non-judgmental support
3. **Empowerment** - Knowledge enables action
4. **Community** - Collective solutions to shared challenges
5. **Accessibility** - Information for all abilities
6. **Safety** - Prioritize user wellbeing
7. **Transparency** - Clear about capabilities and limits

---

## 🤝 Contributing

Want to improve these agents or add new ones?

### Ideas for Contributions
- Add agents for housing, healthcare, legal aid, jobs
- Improve language support for non-English speakers
- Create custom tools for specific calculations
- Enhance accessibility features
- Add testing and validation
- Improve documentation

### How to Contribute
1. Fork the repository
2. Create a new agent following the existing structure
3. Test thoroughly with diverse queries
4. Document your agent
5. Submit a pull request

---

## 📞 Crisis Resources

If you or someone you know is in crisis:

- **National Suicide Prevention Lifeline:** 988 (US)
- **Crisis Text Line:** Text HOME to 741741
- **International:** https://www.iasp.info/resources/Crisis_Centres/
- **Emergency Services:** 911 (US) or your local emergency number

---

## 🐞 Bonus: Debugging Exercise

The **research-agent** is a hands-on debugging exercise with an intentional bug!

```bash
python -m google.adk.cli web agents --log_level DEBUG
# Select "research-agent" and try: "Find latest quantum computing papers"
# Notice the count is way too high!
```

Learn how to use the Events tab and DEBUG logs to find and fix bugs in multi-agent systems.

---

## 🎓 Learning Resources

- [Google ADK Documentation](https://github.com/google/adk)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Docs](https://ai.google.dev/)
- [WCAG Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 📊 Impact Potential

### Individual Level
- Faster access to resources
- Reduced barriers to information
- Increased knowledge and empowerment
- Better decision-making

### Community Level
- More efficient resource distribution
- Increased civic participation
- Stronger community connections
- Collective action on shared challenges

### Systemic Level
- Reduced burden on human services
- Improved accessibility of information
- Democratized access to knowledge
- Scalable support infrastructure

---

## 🌈 Vision

**A world where everyone has easy access to the resources, knowledge, and support they need to thrive.**

These agents represent a step toward:
- More equitable access to information
- Stronger, more connected communities
- Technology serving social good
- Empowered, informed citizens
- Collective action on shared challenges

---

## 📝 License

This project is built with Google's Agent Development Kit and is intended for:
- Educational purposes
- Community benefit
- Nonprofit use
- Research and development
- Social good applications

---

## 🙏 Acknowledgments

Built with:
- Google's Agent Development Kit (ADK)
- Gemini 2.5 Flash Lite model
- Google Search API
- Community input and inspiration

Inspired by:
- Community organizers and advocates
- Social workers and counselors
- Educators and librarians
- Accessibility experts
- Climate activists
- Civic engagement leaders

---

## 🎉 Get Started Now!

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup API key (see SETUP_GUIDE.md)
copy .env.example .env
# Edit .env with your API key

# 3. Launch agents
python -m google.adk.cli web agents --port 8080

# 4. Open http://127.0.0.1:8080 and start making a difference!
```

---

**Together, we can build technology that serves everyone. Let's make a difference! 🌍✨**

---

*For questions, feedback, or contributions, please open an issue or reach out to the community.*
