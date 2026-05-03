import streamlit as st
import joblib

# Load saved TF-IDF and model
tfidf = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("sentiment_model.pkl")

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="💬",
    layout="centered"
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>
body {
    background-color: #eef2f7;
}
.main-title {
    font-size: 40px;
    font-weight: 800;
    color: #2d3436;
    text-align: center;
    margin-bottom: 5px;
}
.sub-text {
    text-align: center;
    color: #636e72;
    font-size: 18px;
    margin-bottom: 30px;
}
.result-box {
    padding: 20px;
    background-color: #ffffff;
    border-radius: 12px;
    border: 2px solid #dfe6e9;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    color: #0984e3;
}
</style>
""", unsafe_allow_html=True)

# ------------------- TITLE -------------------
st.markdown('<div class="main-title">💬 Sentiment Analysis App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Analyze customer reviews instantly with machine learning</div>', unsafe_allow_html=True)

# ------------------- INPUT -------------------
user_input = st.text_area("Write your review here:", height=150)

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        transformed_text = tfidf.transform([user_input])
        prediction = model.predict(transformed_text)[0]

        st.markdown(f'<div class="result-box">Predicted Sentiment: {prediction.upper()}</div>', unsafe_allow_html=True)
