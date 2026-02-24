from crewai import Agent
from backend.llm_config import llm

report_agent = Agent(
    role="Cricket Match Report Generator",
    goal="Generate a detailed and professional match analysis report",
    backstory=(
        "Senior cricket analyst who compiles match insights, player performance, strategy evaluation, "
        "and prediction results into a structured analytical report."
    ),
    llm=llm,
    verbose=True
)