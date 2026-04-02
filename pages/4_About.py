import streamlit as st

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

st.title("ℹ️ About")

st.markdown("""
<div class="glass">
This project analyzes student feedback data to:

• Evaluate teaching quality  
• Identify difficult courses  
• Track satisfaction trends  
• Provide actionable insights  

Built with Python, Pandas, Plotly, Streamlit.
</div>
""", unsafe_allow_html=True)