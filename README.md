# 🎤 AI Interview Practice Tool

Perfect your interview skills with an AI-powered HR interviewer! Get personalized interview questions and receive detailed feedback on your performance - all powered by Google Gemini 2.5 Flash.

## ✨ What Can You Do?

- 🎯 **Practice Real Interviews** - Simulate interviews for your dream job
- 💼 **Choose Your Role** - Data Scientist, Data Engineer, ML Engineer, BI Analyst, or Financial Analyst
- 🏢 **Pick Your Company** - Amazon, Meta, Udemy, LinkedIn, Spotify, and more
- 🤖 **Talk to an AI Interviewer** - Get realistic interview questions based on your background
- 📊 **Get Scored & Reviewed** - Receive a score out of 10 plus detailed feedback
- 🔄 **Practice Unlimited Times** - Keep practicing until you nail it!

## 🚀 Quick Start

### Step 1: Get the Code
```bash
git clone https://github.com/vitaliyarkhanhelski/interview-tool.git
cd interview-tool
```

### Step 2: Set Up Python Environment
We recommend using conda (but you can use venv too):
```bash
conda create -n streamlit-env python=3.10
conda activate streamlit-env
```

### Step 3: Install Dependencies
```bash
pip install streamlit openai streamlit-js-eval
```

### Step 4: Add Your OpenAI API Key
You'll need an OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

1. Create a `.streamlit` folder in the project
2. Inside `.streamlit`, create a file called `secrets.toml`
3. Add this line (replace with your actual key):
   ```toml
   OPEN_API_KEY = "sk-your-actual-api-key-here"
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
   - Choose your level: Junior, Mid-Level, or Senior
   - Select a position (Data Scientist, Engineer, Analyst, etc.)
   - Pick your target company (Amazon, Meta, LinkedIn, etc.)

**3. Start the Interview 🎤**
   - Click "Start Interview"
   - You'll have 3 questions to answer
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
- An OpenAI API key ([sign up for free credits](https://platform.openai.com/signup))
- Internet connection (to connect to OpenAI's API)

That's it! Everything else installs automatically with pip.

## 📁 Project Structure

```
interview-tool/
├── app.py                    # The main app
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

This project is for educational and practice purposes. Feel free to use it to ace your next interview!

## ✍️ Author

**Vitaliy Arkhanhelski**

Happy interviewing! 🎉 Good luck with your job search! 💼

