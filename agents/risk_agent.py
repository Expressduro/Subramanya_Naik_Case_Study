from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import os
from dotenv import load_dotenv

load_dotenv()

class RiskOutput(BaseModel):
    forward_looking_uncertainty: bool
    regulatory_risk: bool
    ethical_risk: bool
    notes: str

risk_agent = Agent(
    model=OpenAIModel(
        "gpt-4o",
        provider=OpenAIProvider(api_key=os.getenv("OPENAI_API_KEY"))
    ),
    output_type=RiskOutput,
    system_prompt=(
        "You are a risk analyst. "
        "Check the article for forward-looking uncertainty, regulatory risks, or ethical risks. "
        "Mark each as True/False and explain why."
    ),
)
