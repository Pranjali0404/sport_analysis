from crewai import Agent
from crewai.tools import tool

from backend.llm_config import llm

from backend.api.cricket_api import (
    get_current_matches,
    get_match_scorecard,
    get_player_info
)

# ---------- TOOLS ----------

@tool("Fetch current matches")
def fetch_current_matches():
    """Return list of currently live or recent cricket matches."""
    return get_current_matches()


@tool("Fetch match scorecard")
def fetch_match_scorecard(match_id: str):
    """Return full scorecard data for the given match ID."""
    return get_match_scorecard(match_id)


@tool("Fetch player info")
def fetch_player_info(player_id: str):
    """Return statistics and profile information of a player."""
    return get_player_info()


# ---------- AGENT ----------

data_agent = Agent(
    role="Cricket Data Collector",
    goal="Fetch structured match and player data",
    backstory="Expert in collecting real-time cricket data from APIs and preparing it for analysis.",
    tools=[
        fetch_current_matches,
        fetch_match_scorecard,
        fetch_player_info
    ],
    llm=llm,
    verbose=True
)