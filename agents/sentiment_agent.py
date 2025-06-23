from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import os
from dotenv import load_dotenv

load_dotenv()

class SentimentOutput(BaseModel):
    sentiment: str = Field(description="positive, neutral, or negative")
    confidence: float = Field(ge=0.0, le=1.0)
    reasoning: str

sentiment_agent = Agent(
    model=OpenAIModel(
        "gpt-4o",
        provider=OpenAIProvider(api_key=os.getenv("OPENAI_API_KEY"))
    ),
    output_type=SentimentOutput,
    system_prompt=(
        "You are a financial sentiment analyzer. "
        "Classify the article as positive, neutral, or negative. "
        "Give a confidence score between 0-1 and reasoning in 1-2 lines."
    ),
)

