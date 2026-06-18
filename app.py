import streamlit as st
import pandas as pd
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\MAMP\htdocs\TelcoCustomerChurn\WA_Fn-UseC_-Telco-Customer-Churn.csv")

model = pickle.load(open('churn_model.pkl', 'rb'))

# Convert TotalCharges
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors='coerce'
)

df.fillna(0, inplace=True)

# Encode categorical columns
le = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# Load trained model
model = pickle.load(open('churn_model.pkl', 'rb'))

# Split
X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Ensure columns match model training columns
X_test = X_test.reindex(
    columns=model.feature_names_in_,
    fill_value=0
)

st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📞",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    div.stButton > button:first-child {
        background-color: #E91E63;
        color: white;
        border-radius: 8px;
        border: none;
        height: 3em;
        font-weight: bold;
    }

    div.stButton > button:first-child:hover {
        background-color: #D81B60;
        color: white;
    }
    
    [data-testid="stSidebar"] {
        min-width: 150px;
        max-width: 150px;
    }
    
    /* Collapsed sidebar width */
    [data-testid="stSidebar"][aria-expanded="false"]{
        min-width: 0px;
        max-width: 0px;
    }

    /* Main content adjustment */
    [data-testid="stSidebar"][aria-expanded="false"] + div {
        margin-left: 0px;
    }
</style>
""", unsafe_allow_html=True)


page = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Prediction",
    ]
)

st.title("📞 Telco Customer Churn Prediction")

if page == "Prediction":
    # Row 1
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Customer Information")

        gender = st.selectbox("Gender", ["Male", "Female"])

    with col2:
        st.subheader(" ")
        
        senior = st.selectbox(
            "Senior Citizen",
            ['No', 'Yes']
        )

    with col3:
        st.subheader(" ")
        
        tenure = st.slider(
            "Tenure (Months)",
            0, 72, 12
        )

    # Row 2
    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader("Billing Information")

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0
        )

    with col5:
        st.subheader(" ")
        
        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0
        )

    with col6:
        st.subheader(" ")
        
        contract = st.selectbox(
            "Contract Type",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

    st.divider()

    gender_map = {
        "Male": 1,
        "Female": 0
    }

    senior_map = {
        "Yes": 1,
        "No": 0
    }

    contract_map = {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    }

    if st.button("Predict Churn"):
        input_data = pd.DataFrame({
            'gender':[gender_map[gender]],
            'SeniorCitizen':[senior_map[senior]],
            'tenure':[tenure],
            'Contract':[contract_map[contract]],
            'MonthlyCharges':[monthly_charges],
            'TotalCharges':[total_charges],
        })
        
        prediction = model.predict(input_data)


        if prediction[0] == 1:
            st.error("⚠️ Customer Likely to Churn")
        else:
            st.success("✅ Customer Likely to Stay")
            
            
        probability = model.predict_proba(input_data)

        st.write(
            f"Churn Probability: {probability[0][1]*100:.2f}%"
        )
        
        st.divider()

if page == "Dashboard": 
    col1, col2 = st.columns(2)
    
    with col1:    
        st.subheader("Customer Churn Distribution")

        fig, ax = plt.subplots(figsize=(6, 4))
        
        sns.countplot(
            x='Churn',
            data=df,
            ax=ax
        )
        ax.set_xticklabels(['No', 'Yes'])

        st.pyplot(fig)
        
    with col2:
        st.subheader("Gender Churn Distribution")

        fig, ax = plt.subplots(figsize=(6, 4))
        
        sns.countplot(x='gender', hue='Churn', data=df, ax=ax)

        ax.set_xticklabels(['No', 'Yes'])
        
        st.pyplot(fig)
        
    col1, col2 = st.columns(2)
    
    with col1:   
        st.subheader("Monthly Charges vs Churn")

        fig, ax = plt.subplots(figsize=(6,4))

        sns.boxplot(
            x='Churn',
            y='MonthlyCharges',
            data=df,
            ax=ax
        )
        ax.set_xticklabels(['No', 'Yes'])
        st.pyplot(fig)
    
    with col2:
        st.subheader("Monthly Charges Distribution")

        fig, ax = plt.subplots(figsize=(6,4))

        sns.histplot(df['MonthlyCharges'], kde=True)
        
        st.pyplot(fig)
        
    col1, col2 = st.columns(2)
    
    with col1:    
        st.subheader("Tenure vs Churn")

        fig, ax = plt.subplots(figsize=(6,4))

        sns.boxplot(
            x='Churn',
            y='tenure',
            data=df,
            ax=ax
        )
        ax.set_xticklabels(['No', 'Yes'])
        st.pyplot(fig)
        
    with col2:  
        st.subheader("Tenure Distribution")

        fig, ax = plt.subplots(figsize=(6,4))

        sns.histplot(df['tenure'], kde=True)

        st.pyplot(fig)

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Contract Type vs Churn")

        fig, ax = plt.subplots(figsize=(6,4))

        sns.countplot(
            x='Contract',
            hue='Churn',
            data=df,
            ax=ax
        )
        ax.set_xticklabels(['Month-to-month','One year','Two year'])
        plt.xticks(rotation=20)

        st.pyplot(fig)
        
    with col2:
        st.subheader("Correlationship")

        fig, ax = plt.subplots(figsize=(6,4))

        df_encoded = df.copy()

        df_encoded.drop(['customerID','Partner','Dependents','PhoneService', 'MultipleLines','InternetService', 'OnlineSecurity', 'OnlineBackup',	'DeviceProtection', 'TechSupport',	'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'PaymentMethod'], axis=1, inplace=True)
        
        for col in df_encoded.select_dtypes(include='object').columns:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col])

        sns.heatmap(df_encoded.corr(), cmap='coolwarm')
        
        st.pyplot(fig)
        
    col1, col2 = st.columns(2)
    
    with col1:
        
        churn_ratio = df['Churn'].value_counts(normalize=True) * 100
        fig, ax = plt.subplots(figsize=(8,4))
    
        plt.pie(
            churn_ratio,
            labels=churn_ratio.index,
            autopct='%1.1f%%'
        )

        plt.title("Actual Churn Ratio")
        plt.show()
        
        st.pyplot(fig)
        
    with col2:
        # Probability of Churn = Yes
        y_prob = model.predict_proba(X_test)[:,1]

        # Sort for smooth sigmoid-like visualization
        sorted_prob = np.sort(y_prob)

        fig, ax = plt.subplots(figsize=(6,4))

        plt.plot(
            range(len(sorted_prob)),
            sorted_prob
        )

        plt.axhline(
            y=0.5,
            linestyle='--',
            label='Threshold = 0.5'
        )

        plt.xlabel("Customers (sorted)", fontsize=14)
        plt.ylabel("Probability of Churn", fontsize=14)
        plt.title("Predicted Probability for Telco Customer Churn", fontsize=16, pad=50)
        plt.legend()
        plt.grid()

        plt.show()
        
        st.pyplot(fig)
