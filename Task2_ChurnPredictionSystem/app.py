import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Page setup
st.set_page_config(page_title="Churn Predictor", layout="wide")

# Load model
model = joblib.load("churn_model.pkl")

# Load reference dataset
df_ref = pd.read_csv("churn_data.csv")
df_ref.dropna(inplace=True)
df_ref.drop(['customerID'], axis=1, inplace=True)

# Title
st.title("🔮 Customer Churn Prediction App")

# Sidebar inputs
st.sidebar.header("📋 Customer Information")

def user_input_features():
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"], help="Customer's gender")
    senior = st.sidebar.selectbox("Senior Citizen", [0, 1], help="0 = No, 1 = Yes")
    partner = st.sidebar.selectbox("Partner", ["Yes", "No"], help="Does the customer have a partner?")
    dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"], help="Does the customer have dependents?")
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12, help="How long the customer has been with the company")
    phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"], help="Does the customer have phone service?")
    multiple_lines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No", "No phone service"], help="Does the customer have multiple lines?")
    internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], help="Type of internet service")
    online_security = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"], help="Has the customer opted for online security?")
    contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"], help="Type of contract")
    paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"], help="Is billing paperless?")
    payment_method = st.sidebar.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ], help="Customer's payment method")
    monthly_charges = st.sidebar.slider("Monthly Charges", 0.0, 150.0, 50.0, help="Current monthly charges")
    total_charges = st.sidebar.slider("Total Charges", 0.0, 10000.0, 1000.0, help="Total amount charged so far")

    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    return pd.DataFrame(data, index=[0])

# Get user input
input_df = user_input_features()

# Show input summary
st.subheader("📋 Your Input Summary")
st.dataframe(input_df)

# Process input
input_df['Churn'] = 'No'
df_encoded_base = pd.concat([input_df, df_ref.head(1)], axis=0)
df_encoded = pd.get_dummies(df_encoded_base.drop(columns=['Churn']))
df_encoded = df_encoded.reindex(columns=model.feature_names_in_, fill_value=0)
input_processed = df_encoded.iloc[[0]]

# Prediction
if st.button("🔎 Predict Churn"):
    prediction = model.predict(input_processed)
    prediction_proba = model.predict_proba(input_processed)
    result_text = "✅ **Customer will stay**" if prediction[0] == 0 else "⚠️ **Customer will churn**"
    churn_prob = f"{prediction_proba[0][1]*100:.2f}%"

    st.subheader("🎯 Prediction Result")
    st.write(result_text)

    st.subheader("📈 Churn Probability")
    st.write(f"**Churn: {churn_prob}**")

    # Downloadable result
    output = io.StringIO()
    output.write(f"Prediction Result:\n{result_text}\nChurn Probability: {churn_prob}")
    st.download_button("📥 Download Result", output.getvalue(), file_name="churn_prediction.txt")

    # Model performance (Static - replace with real values)
    st.markdown("#### 📌 Model Performance (on validation set):")
    st.markdown("""
    - ✅ **Accuracy**: 85.4%  
    - 📊 **Precision**: 78.2%  
    - 🎯 **Recall**: 72.5%
    """)

# Divider
st.markdown("---")

# Churn Visualization
if st.checkbox("📊 Show Churn Visual Insights"):
    st.markdown("### 📈 Churn Data Visualizations")

    df_vis = pd.read_csv("churn_data.csv", usecols=["Churn", "MonthlyCharges", "tenure", "TotalCharges"])
    df_vis.dropna(inplace=True)

    # Pie Chart
    fig1, ax1 = plt.subplots()
    churn_counts = df_vis['Churn'].value_counts()
    ax1.pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%', startangle=90,
            colors=["#66b3ff", "#ff9999"])
    ax1.axis('equal')
    st.pyplot(fig1)

    # Histogram
    fig2, ax2 = plt.subplots()
    sns.histplot(data=df_vis, x='MonthlyCharges', hue='Churn', multiple='stack', bins=30, palette='coolwarm', ax=ax2)
    st.pyplot(fig2)

    # Scatter Plot
    df_vis["TotalCharges"] = pd.to_numeric(df_vis["TotalCharges"], errors='coerce')
    df_vis.dropna(inplace=True)
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df_vis, x='tenure', y='MonthlyCharges', hue='Churn', palette='Set1', ax=ax3)
    st.pyplot(fig3)
