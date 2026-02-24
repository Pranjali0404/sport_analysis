import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
import pandas as pd
import numpy as np

from backend.run_analysis import run_match_analysis

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Sports Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM CSS (SaaS DARK THEME)
# -------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #0F172A;
}

.block-container {
    padding-top: 1.5rem;
}

.metric-card {
    background: #1E293B;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.ai-box {
    background: #1E293B;
    padding: 25px;
    border-radius: 15px;
    border-left: 4px solid #38BDF8;
}

.sidebar-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.markdown("<div class='sidebar-title'>AI Sports Analytics</div>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Match Analysis",
        "Player Analytics",
        "Strategy Planner",
        "Team Management",
        "Reports"
    ]
)

st.sidebar.divider()

team = st.sidebar.selectbox("Select Team", ["India", "Australia", "England", "South Africa"])
match = st.sidebar.selectbox("Select Match", ["Match 1", "Match 2", "Match 3"])

run_analysis = st.sidebar.button("Run AI Analysis")

if st.button("Analyze Match"):
    if match_id:
        with st.spinner("Running AI analysis..."):
            result = run_match_analysis(match_id)

        st.success("Analysis Complete")
        st.write(result)

    else:
        st.warning("Please enter match ID")
if run_analysis:
    st.sidebar.success("Agents Running...")

# -------------------------------------------------
# DUMMY DATA
# -------------------------------------------------
def sample_line_chart():
    data = np.random.randint(3, 10, 20).cumsum()
    df = pd.DataFrame({"Score": data})
    return df


def sample_skill_data():
    return pd.DataFrame({
        "Skill": ['Batting', 'Bowling', 'Fielding', 'Fitness', 'Experience'],
        "Score": np.random.randint(50, 100, 5)
    })

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------
if page == "Dashboard":
    st.title("Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Win Probability", "72%", "+5%")
    with col2:
        st.metric("Team Form", "Good", "+2")
    with col3:
        st.metric("Avg Score", "185", "+12")
    with col4:
        st.metric("Fitness Index", "91%", "+1%")

    st.divider()

    left, right = st.columns([2, 1])

    with left:
        st.subheader("Match Performance Trend")
        st.line_chart(sample_line_chart(), use_container_width=True)

    with right:
        st.subheader("Team Strength Comparison")
        st.bar_chart(sample_skill_data().set_index("Skill"))

    st.divider()

    st.markdown("<div class='ai-box'><h4>AI Insights</h4>Team shows strong batting depth and consistent middle-order performance. Recommended aggressive powerplay strategy.</div>", unsafe_allow_html=True)

# -------------------------------------------------
# MATCH ANALYSIS
# -------------------------------------------------
elif page == "Match Analysis":
    st.title("Match Analysis")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Overview",
        "Score Breakdown",
        "Timeline",
        "Prediction"
    ])

    with tab1:
        st.subheader("Win Probability")
        st.progress(72)
        st.bar_chart(sample_skill_data().set_index("Skill"))

    with tab2:
        st.subheader("Runs Per Over")
        st.line_chart(sample_line_chart(), use_container_width=True)

    with tab3:
        st.subheader("Match Events")
        events = pd.DataFrame({
            "Over": [2, 5, 8, 12, 17],
            "Event": ["Wicket", "Boundary", "Wicket", "Six", "Wicket"]
        })
        st.dataframe(events, use_container_width=True)

    with tab4:
        st.subheader("AI Prediction")
        st.info("Team likely to win if powerplay score exceeds 55 runs.")

# -------------------------------------------------
# PLAYER ANALYTICS
# -------------------------------------------------
elif page == "Player Analytics":
    st.title("Player Analytics")

    player = st.selectbox("Select Player", ["Player A", "Player B", "Player C"])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Skill Comparison")
        st.bar_chart(sample_skill_data().set_index("Skill"))

    with col2:
        st.subheader("Fitness Trend")
        st.line_chart(sample_line_chart(), use_container_width=True)

    st.subheader("Performance Table")

    df = pd.DataFrame({
        "Match": [1,2,3,4,5],
        "Runs": np.random.randint(20,100,5),
        "Strike Rate": np.random.randint(100,160,5)
    })

    st.dataframe(df, use_container_width=True)

# -------------------------------------------------
# STRATEGY PLANNER
# -------------------------------------------------
elif page == "Strategy Planner":
    st.title("AI Strategy Planner")

    st.markdown("<div class='ai-box'><h4>Recommended Strategy</h4>Use spin attack in middle overs. Target opposition weak lower order.</div>", unsafe_allow_html=True)

    st.subheader("Simulation Controls")

    aggression = st.slider("Aggression Level", 0, 100, 60)
    bowling = st.slider("Bowling Rotation", 0, 100, 50)

    if st.button("Recalculate Strategy"):
        st.success("Strategy Updated")

# -------------------------------------------------
# TEAM MANAGEMENT
# -------------------------------------------------
elif page == "Team Management":
    st.title("Team Management")

    squad = pd.DataFrame({
        "Player": ["A", "B", "C", "D"],
        "Role": ["Batsman", "Bowler", "All-rounder", "Bowler"],
        "Fitness": [90, 80, 95, 85],
        "Available": [True, True, False, True]
    })

    st.dataframe(squad, use_container_width=True)

# -------------------------------------------------
# REPORTS
# -------------------------------------------------
elif page == "Reports":
    st.title("Reports & Insights")

    st.markdown("<div class='ai-box'><h4>Match Report</h4>Strong top-order stability and disciplined bowling performance.</div>", unsafe_allow_html=True)

    st.download_button("Download Report PDF", "Sample report content")