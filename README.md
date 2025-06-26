# 📈 Stock Movement Prediction Web Application

Predict the movement of stock prices (Up 📈 or Down 📉) based on news headlines using a simple Machine Learning model, deployed as a web application with **Streamlit**.

---

## 👨‍💻 Team Members

- Sarvesh Patel  
- Ashtha  
- Abdush  
- Arpit  

**Department:** Computer Application  
**University:** Quantum University  
**Date:** 23 May 2025

---

## 🧠 Project Overview

- Automates the prediction of stock market movement using news headlines.
- Uses **Logistic Regression** for classification.
- Deployed as an easy-to-use **web application** with **Streamlit**.
- Provides real-time stock movement predictions based on text input.

---

## ❓ Problem Statement

- The stock market is highly volatile and influenced by daily news.
- Manual interpretation of news is time-consuming and error-prone.
- Our goal: **Automatically predict whether a stock will move Up or Down based on news headlines**.

---

## 📊 Dataset Details

- Total Samples: 1000 news headlines
  - 500 Positive headlines (labeled as "Up")
  - 500 Negative headlines (labeled as "Down")

**Example Headlines:**
- Positive: “Company reports record profits”
- Negative: “Layoffs announced by the company”

---

## 🤖 Machine Learning Model

- **Model Used:** Logistic Regression  
- **Text Preprocessing:** CountVectorizer  
- **Labels:** Up = 1, Down = 0  
- **Training Set Size:** 1000 labeled samples  

---

## 🔄 Data Processing Pipeline

1. **Input:** Raw news headline (text)
2. **Feature Extraction:** Convert text to numeric vectors using CountVectorizer
3. **Model Training:** Logistic Regression
4. **Output:** Predicted movement → Up 📈 or Down 📉

---

## 🌐 Web Application (Built with Streamlit)

- Simple and clean user interface
- Input a news headline
- Instantly receive prediction

### 🔧 How to Run

1. Save the Python file as `stock_predictor_app.py`
2. Open terminal and navigate to the script location
3. Run the following command:

```bash
streamlit run stock_predictor_app.py

