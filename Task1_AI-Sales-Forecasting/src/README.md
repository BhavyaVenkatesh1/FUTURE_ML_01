# 📊 Task 1: AI-Powered Sales Forecasting & Trend Analysis

## 📘 Project Overview
This project demonstrates an end-to-end pipeline for **sales trend analysis** and **future forecasting** using real-world retail data (`train.csv`).  
It leverages both statistical and machine learning techniques to extract insights and predict future sales trends.

Key highlights:
- Exploratory Data Analysis (EDA)
- Linear Regression modeling for trend detection
- Time-series forecasting using **Facebook Prophet**
- Interactive dashboard using **Streamlit**

---

## 🎯 Objectives
- Understand seasonal patterns and sales cycles
- Fit a regression model to analyze long-term sales trends
- Apply Prophet to make accurate time-series forecasts
- Build a simple, user-friendly sales forecasting dashboard

---

## 🛠️ Tools & Technologies
- **Python**: Core programming
- **Libraries**:
  - `pandas`, `matplotlib`, `seaborn`: Data wrangling and visualization
  - `scikit-learn`: Linear regression
  - `prophet`: Time-series forecasting
  - `streamlit`: Interactive dashboard
- **Jupyter Notebook**: Experimentation and EDA

---

## 📁 Folder Structure

Task1_AI-Sales-Forecasting/
├── data/
│ └── archive/
│ └── train.csv
├── notebooks/
│ ├── explore_data.ipynb
│ ├── regression_trend.ipynb
│ └── sales_forecast.ipynb
├── outputs/
│ └── forecast_output.csv
├── src/
│ ├── app.py # Streamlit dashboard
│ ├── requirements.txt
│ └── README.md
└── README.md # This file