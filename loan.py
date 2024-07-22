import pickle
import numpy as np
import streamlit as st
hr_loaded_model = pickle.load(open('D:/anaconda/loan_model.sav', 'rb'))

def lon_pred(loan_input):
    loan_np = np.asarray(loan_input)
    loan_reshape = loan_np.reshape(1,-1)
    prediction = hr_loaded_model.predict(loan_reshape)

    
    if(prediction[0]==0):
        return "loan not approved"
    else:
        return "loan approved"
    
def main():
    st.title('loan prediction web app')

    Gender=st.text_input('Gender')
    Married=st.text_input('Married')
    Dependents=st.text_input('Dependents')
    Education=st.text_input('Education')
    Self_Employed=st.text_input('Self_Employed')
    ApplicantIncome=st.text_input('ApplicantIncome')
    CoapplicantIncome=st.text_input('CoapplicantIncome')
    LoanAmount=st.text_input('LoanAmount')
    Loan_Amount_Term=st.text_input('Loan_Amount_Term')
    Credit_History=st.text_input('Credit_History')
    Property_Area=st.text_input('Property_Area')
    
    Loan_Status = '' 
    
    if st.button('Diagnosis Test Reesult'):
        Loan_Status = lon_pred([ Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])

    st.success(Loan_Status)
    
if __name__ == "__main__":
    main()
