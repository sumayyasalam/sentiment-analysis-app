import streamlit as st
import joblib

tfidf = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("sentiment_model.pkl")

st.title("🔮 Sentiment Prediction")

user_input = st.text_area("Write your review here:", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter text.")
    else:
        transformed = tfidf.transform([user_input])
        prediction = model.predict(transformed)[0]
        st.success(f"Predicted Sentiment: **{prediction.upper()}**")
