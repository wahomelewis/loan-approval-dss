import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.utils import resample
import pickle

# Load data
data = pd.read_excel("data/loan_data_cleaned.xlsx")
data = data.dropna()

# Convert target
data['prior_default'] = data['prior_default'].map({'Yes': 1, 'No': 0})

# Create feature
data['loan_to_income'] = data['loan_amnt'] / (data['person_income'] + 1)

# Balance dataset
majority = data[data['prior_default'] == 0]
minority = data[data['prior_default'] == 1]

minority_upsampled = resample(
    minority,
    replace=True,
    n_samples=len(majority),
    random_state=42
)

data_balanced = pd.concat([majority, minority_upsampled])

# ✅ FINAL FEATURE SET (ONLY 5)
X = data_balanced[[
    'loan_to_income',
    'credit_score',
    'loan_int_rate',
    'emp_years',
    'credit_hist_years'
]]

y = data_balanced['prior_default']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=12,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Save model
pickle.dump(model, open("loan_model.pkl", "wb"))

print("Model saved as loan_model.pkl ✅")