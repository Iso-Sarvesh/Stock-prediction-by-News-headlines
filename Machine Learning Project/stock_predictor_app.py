import streamlit as st
import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Sample positive and negative headlines
positive_headlines = [
    "Company reports record-breaking profits",
    "New product launch exceeds expectations",
    "CEO announces global expansion plans",
    "Strong earnings report boosts investor confidence",
    "Strategic partnership increases market share",
    "Tech stock surges after software upgrade",
    "Biotech firm sees success with clinical trials",
    "Retail giant announces holiday discounts",
    "Automaker sees increased demand for EVs",
    "Government incentives boost company performance",
]

negative_headlines = [
    "Company faces legal action over faulty products",
    "Disappointing earnings report shocks investors",
    "Layoffs announced amid financial struggle",
    "Data breach exposes millions of customer records",
    "CEO resigns amid controversy",
    "Product recall hurts brand reputation",
    "Tech firm loses major client contract",
    "Company under investigation for fraud",
    "Natural disaster disrupts production",
    "Negative analyst rating leads to stock drop",
]

# Create dataset with 1000 rows (500 positive + 500 negative)
expanded_headlines = []
expanded_labels = []

for _ in range(500):
    expanded_headlines.append(random.choice(positive_headlines))
    expanded_labels.append(1)
    expanded_headlines.append(random.choice(negative_headlines))
    expanded_labels.append(0)

df = pd.DataFrame({
    "Headline": expanded_headlines,
    "Label": expanded_labels
})

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["Headline"])
y = df["Label"]
model = LogisticRegression()
model.fit(X, y)

# Streamlit UI
st.set_page_config(page_title="Stock Movement Predictor", layout="centered")
st.markdown("## 📈 Stock Movement Predictor Based on News Headline")
st.markdown("Enter a **news headline** to predict if the stock will go **UP 📈** or **DOWN 📉**")

headline = st.text_input("📰 Enter News Headline:")

if headline:
    X_input = vectorizer.transform([headline])
    prediction = model.predict(X_input)[0]
    result = "📈 STOCK WILL GO UP" if prediction == 1 else "📉 STOCK WILL GO DOWN"
    st.markdown(f"### 🧠 Prediction Result: {result}")
