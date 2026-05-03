import streamlit as st

st.title("📘 Model Information")

st.markdown("""
### 🔧 Model Used
- Logistic Regression  
- TF-IDF Vectorizer  

### 📦 Training Steps
1. Clean text  
2. Tokenize  
3. Convert to TF-IDF  
4. Train Logistic Regression  
5. Save model + vectorizer  

### 🎯 Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  
""")
