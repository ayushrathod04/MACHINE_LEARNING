import pickle
import numpy as np
import streamlit as st

# Load the model
hr_loaded_model = pickle.load(open('D:/anaconda/heart_model.sav', 'rb'))

def hr_pred(input_data):
    input_np = np.asarray(input_data)
    input_reshaped = input_np.reshape(1, -1)
    prediction = hr_loaded_model.predict(input_reshaped)
    if prediction[0] == 0:
        return "No heart disease"
    else:
        return "Heart disease"

def main():
    st.title('Heart Prediction Web App')
    
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Type (CP)')
    trestbps = st.text_input('Resting Blood Pressure (trestbps)')
    chol = st.text_input('Serum Cholestoral in mg/dl (chol)')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (fbs)')
    restecg = st.text_input('Resting Electrocardiographic Results (restecg)')
    thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
    exang = st.text_input('Exercise Induced Angina (exang)')
    oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest (oldpeak)')
    slope = st.text_input('Slope of the Peak Exercise ST Segment (slope)')
    ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (ca)')
    thal = st.text_input('Thalassemia (thal)')
    
    target = ''
    
    if st.button('Diagnosis Test Result'):
        target = hr_pred([
            int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg),
            int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)
        ])
        st.success(target)
    
if __name__ == "__main__":
    main()
