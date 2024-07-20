

import numpy as np
import pickle 
import streamlit as st

loaded_model = pickle.load(open("D:/anaconda/trained_model.sav",'rb'))

def dia_pred(input_data):

    input_data_np = np.asarray(input_data)
    
    input_reshape = input_data_np.reshape(1,-1)
    
    pred = loaded_model.predict(input_reshape)
    print(pred)
    
    if pred[0] == 0:
      return 'Person is non-diabetic'
    else:
      return 'Person is diabetic'
  
def main():
    st.title('Diabetes Prediction Web App')
    
    Pregnancies = st.text_input('Enter no. of Pregnanices:')
    Glucose = st.text_input('Enter Glucose:')
    BloodPressure = st.text_input('Enter Blood Pressure:')
    SkinThickness = st.text_input('Enter Skin Thickness:')
    Insulin = st.text_input('Enter Insulin:')
    BMI = st.text_input('Enter BMI:')
    DiabetesPedigreeFunction = st.text_input('Enter Diabetes Pedigree Function:')
    Age = st.text_input('Enter Age')
    
    diagnosis = ''
    
    if st.button('Diagnosis Test Reesult'):
        diagnosis = dia_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)
    
if __name__ == '__main__':
    main()