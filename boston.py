import streamlit as st
import pickle
import numpy as np


# Load the model
def load_model():
    with open('D:/anaconda/bh_model.sav', 'rb') as file:
        model = pickle.load(file)
    return model

# Define the main function
def main():
    st.title("Boston Housing Price Prediction with XGBoost")
    
    # Load the model
    model = load_model()
    
    # User inputs
    CRIM = st.text_input("Per capita crime rate (CRIM)", "0.00632")
    ZN = st.text_input("Proportion of residential land zoned for lots over 25,000 sq. ft. (ZN)", "18.0")
    INDUS = st.text_input("Proportion of non-retail business acres per town (INDUS)", "2.31")
    CHAS = st.text_input("Charles River dummy variable (CHAS): 1 if tract bounds river; 0 otherwise", "0")
    NOX = st.text_input("Nitric oxides concentration (NOX)", "0.538")
    RM = st.text_input("Average number of rooms per dwelling (RM)", "6.575")
    AGE = st.text_input("Proportion of owner-occupied units built prior to 1940 (AGE)", "65.2")
    DIS = st.text_input("Weighted distances to five Boston employment centers (DIS)", "4.0900")
    RAD = st.text_input("Index of accessibility to radial highways (RAD)", "1")
    TAX = st.text_input("Full-value property tax rate per $10,000 (TAX)", "296")
    PTRATIO = st.text_input("Pupil-teacher ratio by town (PTRATIO)", "15.3")
    B = st.text_input("1000(Bk - 0.63)^2 where Bk is the proportion of African Americans by town (B)", "396.90")
    LSTAT = st.text_input("Percentage of lower status of the population (LSTAT)", "4.98")

    # Convert inputs to numpy array
    input_data = np.array([[float(CRIM), float(ZN), float(INDUS), float(CHAS), float(NOX), 
                            float(RM), float(AGE), float(DIS), float(RAD), float(TAX), 
                            float(PTRATIO), float(B), float(LSTAT)]])
    
    # Prediction
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.write(f"The predicted price of the house is: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    main()
