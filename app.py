import streamlit as st
from src.predict import predict_churn

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn based on service details.")

st.sidebar.header("Customer Information")

gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
senior = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["No", "Yes"])
dependents = st.sidebar.selectbox("Dependents", ["No", "Yes"])
tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)

phone = st.sidebar.selectbox("Phone Service", ["No", "Yes"])
multiple = st.sidebar.selectbox(
    "Multiple Lines",
    ["No", "No phone service", "Yes"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

security = st.sidebar.selectbox(
    "Online Security",
    ["No", "No internet service", "Yes"]
)

backup = st.sidebar.selectbox(
    "Online Backup",
    ["No", "No internet service", "Yes"]
)

device = st.sidebar.selectbox(
    "Device Protection",
    ["No", "No internet service", "Yes"]
)

support = st.sidebar.selectbox(
    "Tech Support",
    ["No", "No internet service", "Yes"]
)

tv = st.sidebar.selectbox(
    "Streaming TV",
    ["No", "No internet service", "Yes"]
)

movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["No", "No internet service", "Yes"]
)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.sidebar.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment = st.sidebar.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

monthly = st.sidebar.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

total = st.sidebar.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)

gender_map = {"Female": 0, "Male": 1}
yes_no = {"No": 0, "Yes": 1}
multiple_map = {"No": 0, "No phone service": 1, "Yes": 2}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
service_map = {"No": 0, "No internet service": 1, "Yes": 2}
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
payment_map = {
    "Bank transfer (automatic)": 0,
    "Credit card (automatic)": 1,
    "Electronic check": 2,
    "Mailed check": 3
}

if st.button("Predict Churn"):

    customer = {
        "gender": gender_map[gender],
        "SeniorCitizen": senior,
        "Partner": yes_no[partner],
        "Dependents": yes_no[dependents],
        "tenure": tenure,
        "PhoneService": yes_no[phone],
        "MultipleLines": multiple_map[multiple],
        "InternetService": internet_map[internet],
        "OnlineSecurity": service_map[security],
        "OnlineBackup": service_map[backup],
        "DeviceProtection": service_map[device],
        "TechSupport": service_map[support],
        "StreamingTV": service_map[tv],
        "StreamingMovies": service_map[movies],
        "Contract": contract_map[contract],
        "PaperlessBilling": yes_no[paperless],
        "PaymentMethod": payment_map[payment],
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    prediction, probability = predict_churn(customer)

    st.divider()

    if prediction == 1:
        st.error("⚠ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

    st.metric("Churn Probability", f"{probability*100:.2f}%")