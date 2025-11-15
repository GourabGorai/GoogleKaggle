# Community-Focused AI Agents

A collection of AI agents designed to benefit larger communities and support important social causes.

## 🌍 Available Agents

### 1. Mental Health Support Agent
**Purpose:** Provide mental health resources, crisis support, and compassionate guidance

**What it does:**
- Shares crisis hotlines and emergency resources
- Provides evidence-based coping strategies
- Helps find local mental health services and support groups
- Offers encouragement while maintaining professional boundaries
- Always prioritizes safety and directs to professional help when needed

**Example queries:**
- "I'm feeling overwhelmed, what resources are available?"
- "Find mental health support groups in my area"
- "What are some evidence-based coping strategies for anxiety?"
- "I need crisis support resources"

**Important:** This agent is NOT a replacement for professional mental health care. It provides information and resources only.

---

### 2. Food Security Helper
**Purpose:** Connect people with food assistance and promote community food resilience

**What it does:**
- Helps locate food banks, pantries, and meal programs
- Provides information about SNAP, WIC, and other assistance programs
- Shares budget-friendly meal planning and cooking tips
- Connects people with community gardens and urban farming
- Offers food preservation and nutrition education

**Example queries:**
- "Find food banks near zip code 10001"
- "How do I apply for SNAP benefits?"
- "Budget meal ideas for a family of four"
- "Community gardens in my area"
- "Food rescue programs near me"

---

### 3. Education Equity Guide
**Purpose:** Make quality education accessible to everyone

**What it does:**
- Connects learners with free educational resources (Khan Academy, Coursera, etc.)
- Helps find scholarships, grants, and financial aid
- Shares tutoring and mentorship programs
- Provides guidance on alternative education pathways
- Supports educational advocacy

**Example queries:**
- "Free online courses for computer science"
- "Scholarships for first-generation college students"
- "Adult education programs in my city"
- "How to apply for FAFSA?"
- "Free tutoring resources for high school students"

---

### 4. Climate Action Helper
**Purpose:** Empower individuals and communities to take climate action

**What it does:**
- Provides practical steps to reduce carbon footprint
- Shares local climate initiatives and volunteer opportunities
- Explains climate science in accessible terms
- Connects people with sustainable living resources
- Helps with climate advocacy and policy engagement

**Example queries:**
- "How can I reduce my carbon footprint?"
- "Climate action groups in my city"
- "Government incentives for solar panels"
- "How to compost at home"
- "Ways to contact my representatives about climate policy"

---

### 5. Accessibility Advocate
**Purpose:** Promote digital accessibility and inclusive design

**What it does:**
- Educates about web accessibility standards (WCAG, ADA)
- Provides guidance for making websites and apps accessible
- Shares resources for assistive technologies
- Helps identify accessibility issues
- Advocates for inclusive design principles

**Example queries:**
- "How do I make my website WCAG compliant?"
- "What are the best screen readers?"
- "Accessibility testing tools for developers"
- "How to write good alt text for images"
- "ADA compliance requirements for websites"

---

### 6. Civic Engagement Guide
**Purpose:** Help people participate in democracy and build stronger communities

**What it does:**
- Helps with voter registration and voting information
- Provides information about local government and representatives
- Shares resources for community organizing
- Connects people with volunteer opportunities
- Explains how government works at all levels
- Promotes informed, active citizenship

**Example queries:**
- "How do I register to vote in my state?"
- "Find my local representatives and their contact info"
- "Upcoming city council meetings in my area"
- "How to organize a community campaign"
- "Volunteer opportunities in my neighborhood"
- "How to submit public comment on a local issue"

---

## 🚀 How to Use These Agents

### Start the Web UI
```bash
python -m google.adk.cli web agents
```

Then open your browser to: **http://127.0.0.1:8000**

Select any of the community agents from the dropdown menu and start chatting!

### Run from Command Line
```bash
# Mental Health Support
python -m google.adk.cli run agents/mental-health-support

# Food Security Helper
python -m google.adk.cli run agents/food-security-helper

# Education Equity Guide
python -m google.adk.cli run agents/education-equity-guide

# Climate Action Helper
python -m google.adk.cli run agents/climate-action-helper

# Accessibility Advocate
python -m google.adk.cli run agents/accessibility-advocate

# Civic Engagement Guide
python -m google.adk.cli run agents/civic-engagement-guide
```

---

## 🎯 Design Principles

All community agents follow these principles:

1. **Accessibility First:** Information should be easy to understand and actionable
2. **Dignity & Respect:** Non-judgmental, compassionate, and empowering
3. **Safety:** Always prioritize user safety and direct to professional help when needed
4. **Evidence-Based:** Share credible, verified information and resources
5. **Community-Focused:** Emphasize collective action and mutual support
6. **Practical:** Provide concrete steps and real resources, not just theory
7. **Inclusive:** Consider diverse backgrounds, abilities, and circumstances

---

## 🔐 Privacy & Safety Notes

- These agents use Google Search to find current, local resources
- No personal information is stored or shared
- For mental health: Always directs to crisis services when appropriate
- For food security: Maintains dignity and avoids stigmatizing language
- For education: Recognizes systemic barriers and promotes equity
- For climate: Focuses on empowerment, not guilt or doom
- For accessibility: Centers disabled voices and lived experiences

---

## 🤝 Contributing

Want to improve these agents or add new community-focused agents? Consider:

- Adding more specific resources for underserved communities
- Improving language support for non-English speakers
- Adding tools for specific calculations (carbon footprint, food budgets, etc.)
- Creating agents for other important causes (housing, healthcare, voting rights, etc.)
- Enhancing accessibility of the agents themselves

---

## 📚 Additional Resources

Each agent can help you find:
- Local organizations and services
- Government programs and benefits
- Community groups and volunteer opportunities
- Educational materials and training
- Advocacy tools and campaigns
- Success stories and inspiration

---

## ⚠️ Important Disclaimers

- **Mental Health Agent:** Not a replacement for professional mental health care
- **Food Security Agent:** Provides information only, not direct food assistance
- **Education Agent:** Cannot guarantee admission or financial aid
- **Climate Agent:** Individual action is important but systemic change is essential
- **Accessibility Agent:** Provides guidance but not legal advice

---

## 🌟 Impact

These agents aim to:
- Reduce barriers to essential resources
- Empower individuals with knowledge and tools
- Build stronger, more resilient communities
- Promote equity and justice
- Make technology work for social good

**Remember:** Technology is a tool. Real change comes from people working together in their communities.

---

## 🔧 Technical Details

- **Model:** Gemini 2.5 Flash Lite
- **Tools:** Google Search for real-time, local information
- **Retry Logic:** Automatic handling of rate limits and errors
- **Session Management:** Maintains conversation context

---

## 📞 Crisis Resources (Always Available)

If you or someone you know is in crisis:

- **National Suicide Prevention Lifeline:** 988 (US)
- **Crisis Text Line:** Text HOME to 741741
- **International:** https://www.iasp.info/resources/Crisis_Centres/
- **Emergency Services:** 911 (US) or your local emergency number

---

*Built with Google's Agent Development Kit (ADK) to serve communities and promote social good.*
