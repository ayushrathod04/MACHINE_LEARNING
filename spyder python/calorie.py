
import pickle
import numpy as np
import streamlit as st
import xgboost

# Load the model
cal_loaded_model = pickle.load(open('D:/anaconda/calorie_model.sav', 'rb'))

def lon_pred(cal_input):
    input_np = np.asarray(cal_input)
    input_reshaped = input_np.reshape(1, -1)
    prediction = cal_loaded_model.predict(input_reshaped)
    return prediction
    
def main():
    st.title('Calorie Prediction Web App')

    Gender = st.text_input('Gender')
    Age = st.text_input('Age')
    Height = st.text_input('Height')
    Weight = st.text_input('Weight')
    Duration = st.text_input('Duration')
    Heart_Rate = st.text_input('Heart Rate')
    Body_Temp = st.text_input('Body Temperature')

    price = '' 
    
    if st.button('Get Prediction'):
        price = lon_pred([int(Gender), int(Age), int(Height), int(Weight), int(Duration), int(Heart_Rate), float(Body_Temp)])

    st.success(price)
    
if __name__ == "__main__":
    main()
