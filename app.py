import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tab1, tab2 = st.tabs(["🔮 Prediction", "📊 EDA"])

with tab1:
    user_input = st.text_area("Write your review here:", height=150)

    if st.button("Predict Sentiment"):
        if user_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            transformed_text = tfidf.transform([user_input])
            prediction = model.predict(transformed_text)[0]

            st.markdown(f'<div class="result-box">Predicted Sentiment: {prediction.upper()}</div>', unsafe_allow_html=True)
with tab2:
    st.subheader("Dataset Overview")

    df =  pd.read_excel("datasetNLP.xlsx")  # If you want to include your dataset

    st.write(df.head())

    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x=df['sentiment'], palette="viridis", ax=ax)
    st.pyplot(fig)

    st.subheader("Review Length Distribution")
    df['length'] = df['review'].apply(len)
    fig2, ax2 = plt.subplots()
    sns.histplot(df['length'], bins=30, kde=True, color="blue", ax=ax2)
    st.pyplot(fig2)
