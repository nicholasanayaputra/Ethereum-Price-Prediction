import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
file_path = "dashboard/ETH_Predictions.csv"
df = pd.read_csv(file_path, parse_dates=["Date"])

# Pisahkan data untuk prediksi masa depan
df_actual_vs_pred = df[df["Actual Price"].notna()]
df_future_pred = df[df["Actual Price"].isna()]

# Future Predictions Table
future_predictions_df = df_future_pred[["Date", "Predicted Price"]]

# Function to plot Actual vs Predicted Prices
def plot_actual_vs_predicted():
    fig, ax = plt.subplots(figsize=(14, 7))
    
    ax.plot(df_actual_vs_pred["Date"], df_actual_vs_pred["Actual Price"], label="Actual ETH Prices", color="#2926ff", linewidth=2.5)
    ax.plot(df_actual_vs_pred["Date"], df_actual_vs_pred["Predicted Price"], label="Predicted ETH Prices", color="red", linewidth=1.5)

    ax.set_title("Actual vs Predicted ETH Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()

    return fig

# Function to plot Actual vs Predicted ETH Prices with Future Predictions
def plot_combined_chart():
    fig, ax = plt.subplots(figsize=(14, 7))

    # Plot actual vs predicted
    ax.plot(df_actual_vs_pred["Date"], df_actual_vs_pred["Actual Price"], label="Actual ETH Prices", color="#2926ff", linewidth=2.5)
    ax.plot(df_actual_vs_pred["Date"], df_actual_vs_pred["Predicted Price"], label="Predicted ETH Prices", color="red", linewidth=1.5)

    # Plot future predictions
    ax.plot(df_future_pred["Date"], df_future_pred["Predicted Price"], label="Future Predictions (Next 30 Days)", color="#808981", linewidth=2.5)

    ax.set_title("Actual vs Predicted ETH Prices with Future Predictions")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()

    return fig

# Streamlit Dashboard
st.title("📊 Ethereum (ETH) Price Prediction Dashboard")

# ✨ Future Predictions (Editable Table) at the TOP
st.subheader("📅 Future ETH Price Predictions (Editable)")
edited_df = st.data_editor(future_predictions_df, num_rows="dynamic")

st.write("🔹 **Adjust the values as needed and analyze the impact!**")

# 📈 Graph: Actual vs Predicted Prices
st.subheader("📈 Actual vs Predicted ETH Prices")
st.pyplot(plot_actual_vs_predicted())

# 🔮 Graph: Actual vs Predicted with Future Predictions
st.subheader("🔮 Actual vs Predicted ETH Prices with Future Predictions")
st.pyplot(plot_combined_chart())
