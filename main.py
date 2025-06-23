import os
from dotenv import load_dotenv
from agents.sentiment_agent import sentiment_agent, SentimentOutput
from agents.impact_agent import market_agent, MarketImpactOutput
from agents.risk_agent import risk_agent, RiskOutput
from pydantic import BaseModel

load_dotenv()

class AnalysisOutput(BaseModel):
    sentiment: SentimentOutput
    market_impact: MarketImpactOutput
    risks: RiskOutput

def analyze_article(article: str) -> AnalysisOutput:
    return AnalysisOutput(
        sentiment=sentiment_agent.run_sync(article).output,
        market_impact=market_agent.run_sync(article).output,
        risks=risk_agent.run_sync(article).output
    )

if __name__ == "__main__":
    article = (
        "TechCorp announced a breakthrough AI chip that could revolutionize processing power. "
        "Investors showed early optimism, although regulatory approval is still pending."
    )
    result = analyze_article(article)
    print(result.model_dump_json(indent=2))
