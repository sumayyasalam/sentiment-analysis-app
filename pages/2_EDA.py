import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Exploratory Data Analysis")

df = pd.read_excel("datasetNLP.xlsx", engine="openpyxl")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Sentiment Distribution")
fig, ax = plt.subplots()
sns.countplot(x=df['sentiment'], palette="viridis", ax=ax)
st.pyplot(fig)

st.subheader("Review Length Distribution")
st.subheader("Distribution of Review Lengths")

fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(df['text_length'], bins=30, kde=True, color='blue', ax=ax)

ax.set_title("Distribution of Review Lengths")
ax.set_xlabel("Number of Characters")
ax.set_ylabel("Count")

st.pyplot(fig)

