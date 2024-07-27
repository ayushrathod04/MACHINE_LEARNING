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

# Main function to run the Streamlit app
def main():
    st.title('Credit Card Fraud Detection')
    st.write('Enter the details of the transaction to check if it is fraudulent.')

    # Feature names based on the dataset
    feature_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 
                     'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 
                     'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

    # Pre-populated input values (you can adjust these as needed)
    predata = {
        'Time': 0.0, 'V1': -1.359807, 'V2': -0.072781, 'V3': 2.536347, 'V4': 1.378155,
        'V5': -0.338321, 'V6': 0.462388, 'V7': 0.239599, 'V8': 0.098698, 'V9': 0.363787,
        'V10': 0.090794, 'V11': -0.551600, 'V12': -0.617800, 'V13': -0.991390, 'V14': -0.311169,
        'V15': 1.468177, 'V16': -0.470400, 'V17': 0.207971, 'V18': 0.025791, 'V19': 0.403993,
        'V20': 0.251412, 'V21': -0.018307, 'V22': 0.277838, 'V23': -0.110474, 'V24': 0.066928,
        'V25': 0.128539, 'V26': -0.189115, 'V27': 0.133558, 'V28': -0.021053, 'Amount': 149.62
    }

    # Collect user inputs for each feature with pre-populated values
    features = []
    for feature in feature_names:
        value = st.text_input(f'{feature}', value=str(predata[feature]))
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

if __name__ == '__main__':
    main()
