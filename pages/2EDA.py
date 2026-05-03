import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Exploratory Data Analysis")

df = pd.read_csv("datasetNLP.csv")

st.subheader("Dataset Preview")
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
