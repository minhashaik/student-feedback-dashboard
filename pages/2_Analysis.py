import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
<style>

/* App background */
            
.stApp {
    background: linear-gradient(135deg, #0a0a0f, #111827);
    color: #e5e7eb;
    font-family: 'Inter', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0d0d12;
}

/* Glass card */
.glass {
    background: rgba(255, 255, 255, 0.04);
    border-radius: 16px;
    padding: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
}

/* Titles */
h1, h2, h3 {
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* Chart container */
.stPlotlyChart {
    border-radius: 16px;
    padding: 10px;
    background: rgba(255,255,255,0.02);
}

/* Remove weird spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

st.title("📈 Deep Analysis")

df = pd.read_csv("data/feedback.csv")

st.subheader("🔍 Correlation")

fig = px.imshow(df.corr(numeric_only=True), text_auto=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 Difficulty vs Satisfaction")

fig2 = px.scatter(
    df,
    x="difficulty",
    y="satisfaction",
    color="course",
    size="hours_spent",
    color_discrete_sequence=px.colors.sequential.Plasma
)

st.plotly_chart(fig2, use_container_width=True)