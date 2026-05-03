import streamlit as st
import joblib

# Load saved TF-IDF and model
tfidf = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("sentiment_model.pkl")

st.title("Sentiment Analysis App")
st.write("Enter a review and the model will predict its sentiment.")

# Text input
user_input = st.text_area("Enter your review here:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform text
        transformed_text = tfidf.transform([user_input])
        
        # Predict
        prediction = model.predict(transformed_text)[0]
        
        # Display result
        st.success(f"Predicted Sentiment: **{prediction.upper()}**")

