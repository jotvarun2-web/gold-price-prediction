import streamlit as st
import pickle
import numpy as np

import pandas as pd

df = pd.read_csv("Gold Price.csv")
df["Date"] = pd.to_datetime(df["Date"])

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Gold Price Prediction",
    page_icon="🥇",
    layout="centered"
)

# ------------------------------
# Load Model
# ------------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# ------------------------------
# Title
# ------------------------------
st.title("🥇 Gold Price Prediction App")
st.write("Predict the Gold Price using Machine Learning.")

st.markdown("---")

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("About")

st.sidebar.info("""
### Gold Price Prediction

Model Used:
- Random Forest Regressor

Input Features:
- Open
- High
- Low
- Volume
- Chg%

Developed using Python + Streamlit
""")

# ------------------------------
# Input Fields
# ------------------------------

open_price = st.number_input(
    "Open Price",
    min_value=0.0,
    format="%.2f"
)

high_price = st.number_input(
    "High Price",
    min_value=0.0,
    format="%.2f"
)

low_price = st.number_input(
    "Low Price",
    min_value=0.0,
    format="%.2f"
)

volume = st.number_input(
    "Volume",
    min_value=0
)

change = st.number_input(
    "Change %",
    format="%.2f"
)

st.markdown("---")

# ------------------------------
# Prediction
# ------------------------------

if st.button("Predict Gold Price"):

    input_data = np.array([[open_price,
                            high_price,
                            low_price,
                            volume,
                            change]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Gold Price = ₹ {prediction[0]:,.2f}")
    st.markdown("---")
st.subheader("📅 Predict Using Date")

selected_date = st.date_input("Select a Date")

if st.button("Predict From Date"):

    row = df[df["Date"] == pd.to_datetime(selected_date)]

    if not row.empty:

        open_price = row.iloc[0]["Open"]
        high_price = row.iloc[0]["High"]
        low_price = row.iloc[0]["Low"]
        volume = row.iloc[0]["Volume"]
        change = row.iloc[0]["Chg%"]

        input_data = np.array([[open_price, high_price, low_price, volume, change]])

        prediction = model.predict(input_data)

        st.success(f"Predicted Gold Price: ₹{prediction[0]:,.2f}")

    else:
        st.error("Date not found in dataset.")