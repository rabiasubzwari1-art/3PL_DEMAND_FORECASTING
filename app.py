import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

st.title("📦 AI-Based Demand Forecasting for 3PL Company")

# Load dataset
df = pd.read_csv("data/logistics_demand.csv")
df['date'] = pd.to_datetime(df['date'])

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Demand trend visualization
st.subheader("📈 Total Demand Over Time")
daily_demand = df.groupby('date')['demand'].sum()

fig, ax = plt.subplots()
ax.plot(daily_demand)
ax.set_xlabel("Date")
ax.set_ylabel("Total Demand")
st.pyplot(fig)

# Feature selection
X = df[['orders', 'active_clients', 'fuel_price', 'is_weekend', 'is_festival']]
y = df['demand']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_scaled, y)

st.subheader("🔮 Predict Next-Day Demand")

orders = st.number_input("Number of Orders", min_value=0, value=1000)
clients = st.number_input("Active Clients", min_value=0, value=120)
fuel = st.number_input("Fuel Price", min_value=0.0, value=95.0)
weekend = st.selectbox("Is it a Weekend?", [0, 1])
festival = st.selectbox("Is it a Festival Day?", [0, 1])

if st.button("Predict Demand"):
    input_data = np.array([[orders, clients, fuel, weekend, festival]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    st.success(f"Predicted Demand: {int(prediction[0])}")
