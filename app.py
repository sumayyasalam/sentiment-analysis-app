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

