import streamlit as st
st.markdown("""
<style>

    /* Main page background */
    .main {
        background-color: #0A3D62; /* Dark Blue */
        color: white;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #0A3D62;
        color: white;
    }

    /* Make all text white */
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: white !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #1B4F72;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #154360;
        color: white;
    }

</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)
# 🎨 COLORFUL THEME
st.markdown("""
<style>

    /* Main background */
    .main {
        background-color: #F0F7FF;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #DCEBFF;
    }

    /* Buttons */
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1C6DD0;
        color: white;
    }

    /* Text input */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 2px solid #4A90E2;
    }

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center; font-size:45px;'>💬 Sentiment Analysis App</h1>
<p style='text-align:center; font-size:18px; color:#636e72;'>
A clean, modern machine learning app for analyzing customer reviews.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### 👋 Welcome!
Use the sidebar to navigate:

- 🔮 **Prediction** — Enter text and get instant sentiment  
- 📊 **EDA** — Explore dataset insights  
- 📘 **Model Info** — Learn how the model works  
""")

