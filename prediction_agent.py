from crewai import Agent
from backend.llm_config import llm

prediction_agent = Agent(
    role="Match Outcome Predictor",
    goal="Predict match winner probability using performance data and strategy",
    backstory=(
        "Sports data scientist specializing in probabilistic modeling and match outcome prediction "
        "based on team strength, player form, and match strategy."
    ),
    llm=llm,
    verbose=True
)