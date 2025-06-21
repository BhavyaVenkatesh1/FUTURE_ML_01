import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Use robust path handling
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'outputs', 'forecast_output.csv'))
df = pd.read_csv(file_path)

# Convert date column
df['ds'] = pd.to_datetime(df['ds'])

# Page config
st.set_page_config(page_title="AI Sales Forecast", layout="wide")

# Title
st.title("AI-Powered Sales Forecast Dashboard")

# Summary metrics
st.subheader("Forecast Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Average Forecast", f"{round(df['yhat'].mean(), 2)}")
col2.metric("Min Forecast", f"{round(df['yhat'].min(), 2)}")
col3.metric("Max Forecast", f"{round(df['yhat'].max(), 2)}")

# Date range selector
st.subheader("Filter Forecast by Date Range")
start_date = st.date_input("Start Date", df["ds"].min().date())
end_date = st.date_input("End Date", df["ds"].max().date())
filtered_df = df[(df["ds"] >= pd.to_datetime(start_date)) & (df["ds"] <= pd.to_datetime(end_date))]

# Line chart
st.subheader("Forecasted Sales (Filtered)")
st.line_chart(filtered_df.set_index("ds")[["yhat"]])

# Data table
st.subheader("Forecast Data")
st.dataframe(filtered_df)

# Download filtered data
st.download_button(
    label="Download Filtered Forecast CSV",
    data=filtered_df.to_csv(index=False),
    file_name="forecast.csv",
    mime="text/csv"
)

# Plot with uncertainty intervals
st.subheader("Forecast with Confidence Intervals")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(filtered_df["ds"], filtered_df["yhat"], label="Forecast", color='blue')
ax.fill_between(filtered_df["ds"], filtered_df["yhat_lower"], filtered_df["yhat_upper"],
                alpha=0.3, label="Confidence Interval", color='skyblue')
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title("Forecast with Confidence Intervals")
ax.legend()
st.pyplot(fig)

# Model info
st.info("This forecast is generated using **Facebook Prophet**, trained on historical sales data.")
