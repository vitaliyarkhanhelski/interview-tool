# ☁️ Salesforce Interview Practice Tool

Perfect your Salesforce interview skills with an AI-powered HR interviewer! Get personalized interview questions and receive detailed feedback on your performance - all powered by Google Gemini 2.5 Flash.

## ✨ What Can You Do?

- 🎯 **Practice Real Salesforce Interviews** - Simulate interviews for your dream Salesforce job
- 💼 **Choose Your Role** - Developer, Architect, Business Analyst, QA Engineer, Admin, Consultant, and more
- 🏢 **Pick Your Company** - Salesforce, Deloitte, Accenture, PwC, Capgemini, and leading Salesforce partners
- 🤖 **Talk to an AI Interviewer** - Get realistic interview questions based on your background
- ⚡ **Real-Time Streaming Responses** - Watch AI responses appear word-by-word like ChatGPT
- 🎨 **Beautiful Salesforce-Themed UI** - Enjoy a modern, polished interface with official Salesforce colors and styling
- 📊 **Get Scored & Reviewed** - Receive a score out of 10 plus detailed feedback
- 🔄 **Practice Unlimited Times** - Keep practicing until you nail it!

## 🚀 Quick Start

### Step 1: Get the Code
```bash
git clone https://github.com/vitaliyarkhanhelski/interview-tool.git
cd prototype_sf_agent
```

### Step 2: Set Up Python Environment
We recommend using conda (but you can use venv too):
```bash
conda create -n streamlit-env python=3.10
conda activate streamlit-env
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit google-genai streamlit-js-eval
```

### Step 4: Add Your Google Gemini API Key
You'll need a Google Gemini API key ([Get one for free here](https://aistudio.google.com/app/apikey))

1. Create a `.streamlit` folder in the project
2. Inside `.streamlit`, create a file called `secrets.toml`
3. Add this line (replace with your actual key):
   ```toml
   GEMINI_API_KEY = "your-gemini-api-key-here"
   ```

**Important:** Don't share or commit this file! It's already in `.gitignore` to keep it safe.

## 💡 How to Use

### Launch the App
```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501`

### Your Interview Journey

**1. Tell Us About Yourself 📝**
   - Your name
   - Your experience (what you've done)
   - Your skills (what you're good at)
   
**2. Pick Your Dream Job 🎯**
   - Select a position with the appropriate level (Junior/Mid/Senior Developer, Architect, Business Analyst, QA Engineer, Admin, Consultant, etc.)
   - Pick your target company (Salesforce, Deloitte, Accenture, PwC, Capgemini, etc.)

**3. Start the Interview 🎤**
   - Click "Start Interview"
   - You'll have 5 questions to answer
   - Watch the AI's responses stream in real-time
   - Just type your responses naturally

**4. Get Your Feedback 📊**
   - Click "Get Feedback" after completing the interview
   - See your score (1-10) and detailed review
   - Learn what you did well and where to improve

**5. Practice Again 🔄**
   - Click "Restart Interview" to try different scenarios
   - Keep practicing until you feel confident!

## 📦 What You Need

- Python 3.10 or higher
- A Google Gemini API key ([get one for free](https://aistudio.google.com/app/apikey))
- Internet connection (to connect to Google's Gemini API)

That's it! Everything else installs automatically with `pip install -r requirements.txt`.

## 📁 Project Structure

```
prototype_sf_agent/
├── app.py                    # The main application
├── prompts.py                # System prompts and instructions
├── constants.py              # Configuration and constants
├── ui_components.py          # Reusable UI components
├── styles.css                # Custom Salesforce-themed styling
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── secrets.toml         # Your API key (never shared!)
├── .gitignore               # Keeps secrets safe
└── README.md                # You are here
```

## 🔒 Security Reminder

**Your API key is private!** 🔐

The `.streamlit/secrets.toml` file is already in `.gitignore`, which means it won't be uploaded to GitHub. Keep it that way!

## 🤝 Contributing

Found a bug? Have an idea? Feel free to open an issue or submit a pull request!

## 📄 License

This project is for educational and practice purposes. Feel free to use it to ace your next Salesforce interview!

## ✍️ Author

**Vitaliy Arkhanhelski**

Happy interviewing! ☁️ Good luck with your Salesforce career! 💼

