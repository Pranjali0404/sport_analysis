from crewai import Agent
from backend.llm_config import llm

player_agent = Agent(
    role="Player Performance Analyst",
    goal="Analyze player statistics and identify strengths, weaknesses, and impact on match outcome",
    backstory=(
        "Cricket analytics specialist who evaluates batting, bowling, and fielding performance "
        "to determine player effectiveness and match influence."
    ),
    llm=llm,
    verbose=True
)