import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load data
df = pd.read_csv("data/processed_customer_churn.csv")

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy : {accuracy:.4f}")

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "models/churn_model.pkl")

print("\nModel saved successfully.")

# --------------------------
# Confusion Matrix
# --------------------------

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, predictions)
)

disp.plot()

os.makedirs("screenshots", exist_ok=True)

plt.savefig("screenshots/confusion_matrix.png")

print("Confusion Matrix saved.")

# --------------------------
# Feature Importance
# --------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Important Features\n")

print(importance)

plt.figure(figsize=(10,6))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("screenshots/feature_importance.png")

print("Feature Importance saved.")