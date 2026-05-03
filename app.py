import streamlit as st

st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)


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
