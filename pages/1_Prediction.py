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

st.markdown("---")
st.subheader("📁 Upload File for Prediction")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        
        df = pd.read_excel(uploaded_file, engine="openpyxl")


    st.success("File uploaded successfully!")
    st.write("Preview of uploaded file:")
    st.write(df.head())

    # Let user choose which column contains reviews
    text_columns = df.select_dtypes(include=['object']).columns.tolist()
    selected_col = st.selectbox("Select the column containing reviews", text_columns)

    # Let user choose a specific review
    selected_review = st.selectbox("Choose a review to analyze", df[selected_col].astype(str).tolist())

    if st.button("Predict Sentiment from File"):
        prediction = model.predict([selected_review])[0]
        st.subheader("Prediction Result")
        st.write(f"**Sentiment:** {prediction}")


