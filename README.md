# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a customer is likely to leave a service based on historical customer data. The project uses classification algorithms to analyze customer behavior and provides predictions through an interactive Streamlit web application.

---

## 🚀 Features

- Predicts customer churn (Stay or Churn)
- Data preprocessing and cleaning
- Random Forest Classifier for prediction
- Logistic Regression model comparison
- Model evaluation using:
  - Accuracy Score
  - Classification Report
  - Confusion Matrix
- Feature Importance Visualization
- Interactive Streamlit web application
- Well-structured project for GitHub portfolio

---

## 📂 Project Structure

```text
Customer_Churn_Prediction/
│
├── data/
│   ├── customer_churn.csv
│   └── processed_customer_churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── screenshots/
│   ├── confusion_matrix.png
│   └── feature_importance.png
│
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

## 📊 Machine Learning Workflow

1. Load the customer churn dataset.
2. Clean and preprocess the data.
3. Encode categorical features.
4. Split the dataset into training and testing sets.
5. Train a Random Forest Classifier.
6. Evaluate the model using classification metrics.
7. Save the trained model.
8. Predict customer churn through the Streamlit application.

---

## 📈 Model Evaluation

The model performance is evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Feature Importance Analysis

---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd Customer_Churn_Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Preprocess the dataset

```bash
python src/preprocess.py
```

### Step 2: Train the model

```bash
python src/train_model.py
```

### Step 3: Launch the Streamlit application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## 📁 Dataset

This project uses the IBM Telco Customer Churn dataset, which contains customer demographics, account information, and service usage details for predicting customer churn.

---

## 📷 Screenshots

You can add screenshots of:

- Home Page
- Prediction Result
- Confusion Matrix
- Feature Importance Chart

inside the `screenshots/` folder.

---

## 🔮 Future Enhancements

- Hyperparameter tuning
- Cross-validation
- Advanced feature engineering
- Cloud deployment
- Prediction history
- Download prediction results as CSV
- Docker support

---

## 📄 License

This project is licensed under the MIT License.
