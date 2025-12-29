import streamlit as st
import joblib
import numpy as np

model = joblib.load("co2_model.pkl")

st.title("CO2 Emission Prediction")

engine = st.number_input("Engine Size (L)")
fuel = st.number_input("Fuel Consumption (L/100km)")
weight = st.number_input("Vehicle Weight (kg)")

if st.button("Predict CO2 Emission"):
    prediction = model.predict([[engine, fuel, weight]])
    st.success(f"Estimated CO2 Emission: {prediction[0]:.2f} g/km")
