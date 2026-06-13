# 📞 Telco Customer Churn Prediction

A Machine Learning web application built using Streamlit to predict whether a telecom customer is likely to churn based on customer demographics, account information, and billing details.

---

## 📌 Project Overview

Customer churn is one of the major challenges faced by telecom companies. This project uses Machine Learning techniques to identify customers who are likely to leave the service, enabling businesses to take proactive retention measures.

The application allows users to enter customer details and receive a churn prediction along with the probability score.

---

## 🎯 Problem Statement

Predict whether a customer will:

- Stay with the telecom company
- Churn (leave the company)

This is a **Binary Classification Problem**.

---

## 📊 Dataset

**Dataset:** Telco Customer Churn Dataset

Features include:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges

**Target Variable:**

- Churn (Yes / No)

---

## 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Churn Distribution
- Contract Type vs Churn
- Tenure vs Churn
- Monthly Charges vs Churn
- Payment Method vs Churn
- Correlation Analysis

### Key Insights

- Customers with Month-to-Month contracts showed higher churn rates.
- Customers with shorter tenure were more likely to churn.
- Higher monthly charges were associated with increased churn.
- Long-term contract customers were less likely to leave.

---

## ⚙️ Data Preprocessing

- Removed irrelevant features
- Handled missing values
- Converted data types
- Label Encoding
- Feature Selection
- Train-Test Split

---

## 🤖 Machine Learning Model

### Algorithm Used

- Logistic Regression

### Model Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Results

| Metric | Score |
|----------|----------|
| Accuracy | 81.6% |
| Recall | 82% |
| F1 Score | 64% |

---

## 🖥️ Streamlit Application

Features:

- Customer Churn Prediction
- Probability Score Display
- User-Friendly Interface
- Real-Time Predictions

### Application Screenshot

_Add screenshots here_

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## 📂 Project Structure

```text
TelcoCustomerChurn/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
├── Telco-Customer-Churn.csv
├── notebooks/
│   └── Telco_Customer_Churn.ipynb
├── assets/
│   └── screenshots/
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd TelcoCustomerChurn
```

### Create Virtual Environment

```bash
python -m venv clientenv
```

### Activate Environment

#### Windows

```bash
clientenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Random Forest Classifier
- XGBoost Classifier
- Hyperparameter Tuning
- Feature Importance Visualization
- Deployment on Streamlit Cloud
- Customer Retention Recommendation System

---

## 💡 Business Impact

This solution helps telecom companies:

- Identify customers likely to churn
- Improve customer retention strategies
- Reduce revenue loss
- Increase customer satisfaction

---

## 👨‍💻 Author

**Sathish C**

Aspiring Data Scientist passionate about Machine Learning, Data Analysis, and AI-driven solutions.

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!