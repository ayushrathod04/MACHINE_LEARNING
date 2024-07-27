import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('D:/anaconda/credit_card_model.sav', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_fraud(input_data):
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title('Credit Card Fraud Detection')

# Feature names based on the dataset
feature_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 
                 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 
                 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

# Collect user inputs for each feature
features = []
for feature in feature_names:
    value = st.text_input(f'Enter {feature}')
    features.append(value)

if st.button('Predict'):
    try:
        # Convert inputs to float and create input array
        input_data = [float(f) for f in features]
        result = predict_fraud(input_data)
        
        if result == 1:
            st.write('This transaction is predicted to be **fraudulent**.')
        else:
            st.write('This transaction is predicted to be **non-fraudulent**.')
    except ValueError:
        st.write("Please enter valid numeric values for all features.")
