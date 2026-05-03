{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "67c4246e-0d8a-4284-984b-985ddac4873e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\anaconda3\\anaconda1\\Lib\\site-packages\\pandas\\core\\computation\\expressions.py:22: UserWarning: Pandas requires version '2.10.2' or newer of 'numexpr' (version '2.8.7' currently installed).\n",
      "  from pandas.core.computation.check import NUMEXPR_INSTALLED\n",
      "C:\\Users\\HP\\anaconda3\\anaconda1\\Lib\\site-packages\\pandas\\core\\arrays\\masked.py:56: UserWarning: Pandas requires version '1.4.2' or newer of 'bottleneck' (version '1.3.7' currently installed).\n",
      "  from pandas.core import (\n",
      "2026-05-03 13:34:16.478 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\anaconda3\\anaconda1\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-05-03 13:34:16.487 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "\n",
    "# Load saved TF-IDF and model\n",
    "tfidf = joblib.load(\"tfidf_vectorizer.pkl\")\n",
    "model = joblib.load(\"sentiment_model.pkl\")\n",
    "\n",
    "st.title(\"Sentiment Analysis App\")\n",
    "st.write(\"Enter a review and the model will predict its sentiment.\")\n",
    "\n",
    "# Text input\n",
    "user_input = st.text_area(\"Enter your review here:\")\n",
    "\n",
    "if st.button(\"Predict Sentiment\"):\n",
    "    if user_input.strip() == \"\":\n",
    "        st.warning(\"Please enter some text.\")\n",
    "    else:\n",
    "        # Transform text\n",
    "        transformed_text = tfidf.transform([user_input])\n",
    "        \n",
    "        # Predict\n",
    "        prediction = model.predict(transformed_text)[0]\n",
    "        \n",
    "        # Display result\n",
    "        st.success(f\"Predicted Sentiment: **{prediction.upper()}**\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf75da6f-cfd8-4c25-9375-4c5bbb607fe5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (base)",
   "language": "python",
   "name": "base"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
