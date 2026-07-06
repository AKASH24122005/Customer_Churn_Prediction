import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/customer_churn.csv")

# Remove customerID
if "customerID" in df.columns:
    df.drop(columns=["customerID"], inplace=True)

# Convert TotalCharges
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Encode categorical columns
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "object" or df[col].dtype == "string" or str(df[col].dtype) == "str":
        df[col] = le.fit_transform(df[col].astype(str))

# Alternative safe method
for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

print("\nFinal Data Types:")
print(df.dtypes)

df.to_csv("data/processed_customer_churn.csv", index=False)

print("\nProcessed dataset saved successfully!")