import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import numpy as np

# 🎨 STYLE
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

# HEADER
st.markdown("""
<div style="text-align:center; margin-bottom:30px;">
    <h1>🎓 Student Feedback Dashboard</h1>
    <p style="color:#9ca3af;">Clean insights. Smart decisions.</p>
</div>
""", unsafe_allow_html=True)

df = pd.read_csv("data/feedback.csv")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
    

# FILTERS
course = st.sidebar.selectbox("Course", ["All"] + list(df["course"].unique()))
teacher = st.sidebar.selectbox("Teacher", ["All"] + list(df["teacher"].unique()))

filtered_df = df.copy()

if course != "All":
    filtered_df = filtered_df[filtered_df["course"] == course]
if teacher != "All":
    filtered_df = filtered_df[filtered_df["teacher"] == teacher]

# KPI CARDS
col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="glass">
<h4>⭐ Satisfaction</h4>
<h2>{round(filtered_df["satisfaction"].mean(),2)}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="glass">
<h4>📚 Difficulty</h4>
<h2>{round(filtered_df["difficulty"].mean(),2)}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="glass">
<h4>⏱ Study Hours</h4>
<h2>{round(filtered_df["hours_spent"].mean(),2)}</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# CHARTS
fig1 = px.bar(
    filtered_df,
    x="course",
    y="satisfaction",
    color="course",
    color_discrete_sequence=px.colors.sequential.Plasma,
)

fig2 = px.scatter(
    filtered_df,
    x="difficulty",
    y="satisfaction",
    color="course",
    size="hours_spent",
    color_discrete_sequence=px.colors.sequential.Plasma,
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

# BOX
fig3 = px.box(
    filtered_df,
    x="course",
    y="hours_spent",
    color="course",
    color_discrete_sequence=px.colors.sequential.Plasma,
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("## 🤖 Predict Student Satisfaction")

col1, col2, col3 = st.columns(3)

with col1:
    difficulty = st.slider("Difficulty", 1.0, 5.0, 3.0)

with col2:
    hours = st.slider("Study Hours", 1.0, 10.0, 5.0)

with col3:
    teaching = st.slider("Teaching Quality", 1.0, 5.0, 3.0)

if st.button("Predict Satisfaction"):
    input_data = np.array([[difficulty, hours, teaching]])
    prediction = model.predict(input_data)[0]

    if prediction >= 4:
        st.success(f"🔥 High Satisfaction Expected: {round(prediction,2)}")
    elif prediction >= 3:
        st.info(f"🙂 Moderate Satisfaction: {round(prediction,2)}")
    else:
        st.error(f"⚠ Low Satisfaction Risk: {round(prediction,2)}")