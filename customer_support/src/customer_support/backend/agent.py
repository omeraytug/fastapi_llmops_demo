from pydantic_ai import Agent
from constants import MODEL_MEDIUM
from dotenv import load_dotenv

load_dotenv()

support_agent = Agent(
    model=MODEL_MEDIUM, system_prompt="You are a support agent"
)