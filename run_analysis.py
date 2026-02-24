from backend.crew.sports_crew import sports_crew

def run_match_analysis(match_id: str):
    """
    Called by Streamlit UI.
    Sends match_id to CrewAI and returns final report.
    """

    result = sports_crew.kickoff(
        inputs={"match_id": match_id}
    )

    return result