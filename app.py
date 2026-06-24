import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_model_compressed.pkl")

# Page Config
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to predict whether the transaction is Fraudulent or Legitimate.")

st.markdown("---")

# Input Fields
amt = st.number_input("Transaction Amount", min_value=0.0)

lat = st.number_input("Customer Latitude")

long = st.number_input("Customer Longitude")

city_pop = st.number_input("City Population", min_value=0)

unix_time = st.number_input("Unix Time", min_value=0)

merch_lat = st.number_input("Merchant Latitude")

merch_long = st.number_input("Merchant Longitude")

# Prediction Button
if st.button("Predict Transaction"):

    features = pd.DataFrame({
        'amt': [amt],
        'lat': [lat],
        'long': [long],
        'city_pop': [city_pop],
        'unix_time': [unix_time],
        'merch_lat': [merch_lat],
        'merch_long': [merch_long]
    })

    prediction = model.predict(features)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")

st.markdown("---")
st.caption("CodeSoft Machine Learning Internship - Task 2")