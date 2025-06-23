# 🧠 Financial News Impact Analyzer — Multi-Agent System (Draconic AI Case Study)

This project is a **multi-agent AI system** built using `pydantic-ai` and OpenAI's GPT-4o model to analyze the financial impact of news articles. It simulates how a team of AI agents can collaboratively:

- Determine the sentiment of a news article
- Predict its market impact
- Flag any forward-looking, regulatory, or ethical risks

---

## 📌 Problem Statement

Given financial news articles, build an AI system that can intelligently route them through multiple specialized agents to output structured, explainable insights. The goal is to mirror how analysts evaluate sentiment, impact, and risk — but using agents.

---

## 📁 Project Structure

├── agents/
│ ├── sentiment_agent.py # Agent for classifying sentiment
│ ├── impact_agent.py # Agent for predicting market impact
│ └── risk_agent.py # Agent for risk analysis
├── evaluation/
│ ├── test_cases.json # 5 sample financial news test articles
│ └── run_tests.py # Script to evaluate all test cases
├── main.py # Central orchestrator for single article analysis
├── .env # Your OpenAI API key (keep secret)
├── requirements.txt # All dependencies
└── README.md #


---

## 🛠 Installation & Setup

> 📦 Prerequisites:
> - Python 3.8+
> - OpenAI API key
> - `git` installed

 ✅ Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

✅ Create .env file:

echo OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx > .env
✅ Create virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
✅ Install dependencies:

pip install -r requirements.txt
🚀 How to Run
🔹 Run the multi-agent analyzer on a single articlebash

python main.py
This will print structured output for sentiment, market impact, and risks.

🔹 Run all 5 test cases (from PDF)

python evaluation/run_tests.py
This runs the system on real-world-like examples and prints JSON results.

🤖 Agents Description
Agent	Description
SentimentAgent	Analyzes whether the article tone is positive, negative, or neutral. Includes confidence and reasoning.
MarketImpactAgent	Predicts the likely market reaction (high/medium/low) with justification.
RiskFlagAgent	Flags forward-looking uncertainty, regulatory, or ethical concerns. Returns structured booleans + notes.

Each agent uses pydantic_ai.Agent() with its own prompt and output schema.

✅ Test Case Insights
We tested on 5 diverse articles:

✅ Tesla profits with Musk warning — flagged uncertainty

✅ Amazon AGI investment — flagged regulatory risk

✅ ByteDance — sentiment positive but regulatory risk true

✅ CureGen FDA approval — skepticism caught, impact medium

✅ FirstState Bank — accurate earnings call analysis

All agents returned structured outputs with high consistency.

🧪 Evaluation Summary
Clear agent separation = high explainability

Strict Pydantic schemas reduced hallucinations

Prompts iteratively refined for reliability

Risk agent improved drastically after 3rd iteration

System gracefully handles ambiguity (e.g., speculative news)

📬 Submission Checklist
 Working code with prompt-engineered agents

 5 test cases implemented in JSON

 Documented architecture, reasoning, and outputs

 Chat history and PDF report prepared

 All code split for clarity and modularity

💡 Future Enhancements
Add GUI or Streamlit interface

Add more metrics (F1-score against labeled data)

Visualize risk score trends
