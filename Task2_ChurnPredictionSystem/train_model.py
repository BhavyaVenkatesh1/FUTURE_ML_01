import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load the dataset
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "churn_data.csv"))

X = df.drop("Churn", axis=1)
y = df["Churn"]

# Encode categorical variables if necessary
X = pd.get_dummies(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "churn_model.pkl")
print("Model trained and saved as churn_model.pkl")
