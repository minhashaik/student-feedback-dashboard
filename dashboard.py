import streamlit as st

st.set_page_config(page_title="Student Dashboard", layout="wide")

# 🔒 Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# 🎨 CLEAN PROFESSIONAL STYLE
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(180deg, #0a0a0f, #111827);
    color: #e5e7eb;
    font-family: 'Inter', sans-serif;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 600;
    margin-top: 120px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 15px;
    margin-top: 8px;
    margin-bottom: 50px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 48px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    color: #e5e7eb;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s ease;
}

/* Hover (safe accent) */
.stButton > button:hover {
    background: rgba(255,255,255,0.08);
    border: 1px solid #6366f1;
    transform: translateY(-2px);
}

/* Remove weird padding */
.block-container {
    padding-top: 0;
}

</style>
""", unsafe_allow_html=True)

# 🎯 TITLE
st.markdown('<div class="title">Student Feedback Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">insight over noise</div>', unsafe_allow_html=True)

# 🎮 PERFECT CENTERED BUTTON GRID
left, center, right = st.columns([1, 2, 1])

with center:
    cols = st.columns(4)

    labels = ["Dashboard", "Analysis", "Data", "About"]
    pages = [
        "pages/1_Dashboard.py",
        "pages/2_Analysis.py",
        "pages/3_Data.py",
        "pages/4_About.py"
    ]

    for i in range(4):
        with cols[i]:
            if st.button(labels[i], use_container_width=True):
                st.switch_page(pages[i])

# 🧠 FOOTER
st.markdown("""
<div style="text-align:center; margin-top:80px; color:#6b7280; font-size:13px;">
    built with intent
</div>
""", unsafe_allow_html=True)
# ghnjbdfghjkmnbvcfghjk