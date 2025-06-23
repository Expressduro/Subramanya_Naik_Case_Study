

---

```markdown
# 🧠 Financial News Impact Analyzer — Multi-Agent System (Draconic AI Case Study)

This project implements a **multi-agent AI system** using `pydantic-ai` and OpenAI's GPT-4o to analyze financial news articles. It simulates a team of specialized agents to:

- Determine the **sentiment** of the article
- Predict its **market impact**
- Flag **risks** such as forward-looking statements, regulatory red flags, or ethical concerns

---

## 📌 Problem Statement

Given financial news articles, the system must route them through specialized agents to produce structured insights—much like how real analysts evaluate finance-related narratives.

---

## 📁 Project Structure

```

your-name-case-study/
├── agents/
│   ├── sentiment\_agent.py         # Sentiment classifier
│   ├── impact\_agent.py            # Market impact predictor
│   └── risk\_agent.py              # Risk flagging agent
├── evaluation/
│   ├── test\_cases.json            # 5 news article test cases
│   └── run\_tests.py               # Script to evaluate agents on test data
├── main.py                        # Central orchestrator (uses all 3 agents)
├── .env                           # Contains your OpenAI API key
├── requirements.txt               # Required dependencies
└── README.md                      # You're reading it

````

---

## 🛠️ Installation & Setup

> Requirements: Python 3.8+, OpenAI API key, Git

### 🔹 Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 🔹 Create `.env` file

```bash
echo OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx > .env
```

### 🔹 Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
```

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### ▶️ Run on a Single Article

```bash
python main.py
```

### 🧪 Run on All Test Cases

```bash
python evaluation/run_tests.py
```

> The results for all five test articles will be printed in structured JSON format.

---

## 🧠 Agent Roles

| Agent               | Task                                                                |
| ------------------- | ------------------------------------------------------------------- |
| `SentimentAgent`    | Classifies article tone as positive/neutral/negative + confidence.  |
| `MarketImpactAgent` | Predicts article's market impact (high, medium, low) + explanation. |
| `RiskFlagAgent`     | Flags forward-looking, regulatory, or ethical risks (True/False).   |

Each agent is independently prompted and returns strict, typed responses using Pydantic models.

---

## 📊 Test Case Highlights

| ID      | Notable Behaviors                                                             |
| ------- | ----------------------------------------------------------------------------- |
| FIN-001 | Musk's warning flagged as forward-looking uncertainty                         |
| FIN-002 | FDA approval news = positive sentiment, but impact = medium due to skepticism |
| FIN-003 | AGI announcement flagged high impact + regulatory risk                        |
| FIN-004 | Strong bank earnings but risk = low (correct)                                 |
| FIN-005 | ByteDance growth + regulatory clouds = risk flagged                           |

---

## ✅ Evaluation Summary

* 💡 **Specialized agents** = modularity & clarity
* 🔍 **Prompt engineering** refined through 3 iterations per agent
* ✅ **All test cases returned complete, structured responses**
* 🔄 **Risk and sentiment often aligned; agents worked in tandem**
* 🧪 **Run-time evaluation framework** helps debug + extend easily

---

## 💡 Future Work

* Add Streamlit UI or dashboard
* Allow CSV batch input
* Score performance vs labeled dataset
* Add agent confidence thresholding logic

---





💡 Future Enhancements
Add GUI or Streamlit interface

Add more metrics (F1-score against labeled data)

Visualize risk score trends
