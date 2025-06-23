from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import os
from dotenv import load_dotenv

load_dotenv()

class MarketImpactOutput(BaseModel):
    impact: str = Field(description="high, medium, or low")
    confidence: float = Field(ge=0.0, le=1.0)
    justification: str

market_agent = Agent(
    model=OpenAIModel(
        "gpt-4o",
        provider=OpenAIProvider(api_key=os.getenv("OPENAI_API_KEY"))
    ),
    output_type=MarketImpactOutput,
    system_prompt=(
        "You are a market impact predictor. "
        "Estimate if the article will have a high, medium, or low impact on the market. "
        "Provide confidence and a short justification."
    ),
)
