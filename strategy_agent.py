from crewai import Agent
from backend.llm_config import llm

strategy_agent = Agent(
    role="Match Strategy Expert",
    goal="Design optimal match strategy based on player form and match situation",
    backstory=(
        "Experienced cricket strategist who develops game plans including batting order, "
        "bowling rotations, and tactical adjustments based on match conditions."
    ),
    llm=llm,
    verbose=True
)