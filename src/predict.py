import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/churn_model.pkl")


def predict_churn(input_data):
    """
    Predict whether a customer will churn.

    Parameters:
        input_data (dict): Dictionary containing customer details.

    Returns:
        prediction (int): 0 = No Churn, 1 = Churn
        probability (float): Probability of churn
    """

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return prediction, probability