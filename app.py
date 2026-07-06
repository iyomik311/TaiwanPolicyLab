import streamlit as st
import pandas as pd

from game import TaiwanGame
from simulator import TaiwanSimulator
from nash import calculate_nash, format_equilibria
from charts import plot_average_scores, plot_total_scores
from risk import calculate_risk, risk_level
from silicon import calculate_shield, shield_level
from economy import calculate_cost, cost_level
from analysis import generate_analysis


st.set_page_config(
    page_title="Taiwan Strait Policy Lab",
    page_icon="🌏",
    layout="wide"
)

st.title("🌏 Taiwan Strait Policy Lab")

st.write(
    """
    Game Theory Simulation of Cross-Strait Relations

    Change policy variables and observe how
    the payoff matrix and Nash Equilibrium change.
    """
)

st.sidebar.header("Policy Settings")

us_support = st.sidebar.slider(
    "US Military Support",
    0,
    10,
    5
)

china_pressure = st.sidebar.slider(
    "China Military Pressure",
    0,
    10,
    5
)

taiwan_position = st.sidebar.slider(
    "Taiwan Independence Position",
    0,
    10,
    5
)
semiconductor = st.sidebar.slider(
    "Semiconductor Dependence",
    0,
    100,
    70
)

economic = st.sidebar.slider(
    "Economic Interdependence",
    0,
    100,
    60
)

sanctions = st.sidebar.slider(
    "International Sanctions",
    0,
    100,
    40
)
if st.button("Run Simulation"):

    game = TaiwanGame(
        us_support,
        china_pressure,
        taiwan_position
    )

    us_matrix, china_matrix = game.payoff_matrix()

    st.subheader("US Payoff Matrix")
    st.dataframe(pd.DataFrame(us_matrix))

    st.subheader("China Payoff Matrix")
    st.dataframe(pd.DataFrame(china_matrix))

    equilibria = calculate_nash(
        us_matrix,
        china_matrix
    )

    st.subheader("Nash Equilibria")

    for eq in format_equilibria(equilibria):
        st.success(eq)

    simulator = TaiwanSimulator(
        us_support,
        china_pressure,
        taiwan_position
    )

    results = simulator.run(100)
risk = calculate_risk(
    us_support,
    china_pressure,
    taiwan_position,
    semiconductor,
    economic,
    sanctions
)

shield = calculate_shield(
    semiconductor,
    economic,
    sanctions
)

economic_cost = calculate_cost(
    risk,
    semiconductor,
    economic
)
    st.subheader("Simulation Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "US Average",
            round(results["US Average"], 2)
        )

    with col2:
        st.metric(
            "China Average",
            round(results["China Average"], 2)
        )

    st.pyplot(plot_average_scores(results))

    st.pyplot(plot_total_scores(results))
st.subheader("Policy Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Escalation Risk",
        f"{risk}/100"
    )
    st.caption(risk_level(risk))

with col2:
    st.metric(
        "Silicon Shield",
        f"{shield}/100"
    )
    st.caption(shield_level(shield))

with col3:
    st.metric(
        "Economic Cost",
        f"{economic_cost}%"
    )
    st.caption(cost_level(economic_cost))
    st.subheader("Simulation History")

    st.dataframe(
        pd.DataFrame(results["History"])
    )
st.subheader("AI Policy Analysis")

st.info(
    generate_analysis(
        risk,
        shield,
        economic_cost
    )
)
