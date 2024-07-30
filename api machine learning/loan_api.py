# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:49:41 2024

@author: pf3s1
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    Gender : int 
    Married : int 
    Dependents : int 
    Education : int 
    Self_Employed : int 
    ApplicantIncome : int 
    CoapplicantIncome : float 
    LoanAmount : float 
    Loan_Amount_Term : float 
    Credit_History : float 
    Property_Area : int 
        
loaded_model = pickle.load(open('D:/anaconda/loan_model.sav','rb'))

@app.post('/loan_prediction')

def dia_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)
    
    Gender = input_dict['Gender']
    Married = input_dict['Married']
    Dependents = input_dict['Dependents']
    Education = input_dict['Education']
    Self_Employed = input_dict['Self_Employed']
    ApplicantIncome = input_dict['ApplicantIncome']
    CoapplicantIncome = input_dict['CoapplicantIncome']
    LoanAmount = input_dict['LoanAmount']
    Loan_Amount_Term = input_dict['Loan_Amount_Term']
    Credit_History = input_dict['Credit_History']
    Property_Area = input_dict['Property_Area']
    
    input_list = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]
    
    pred = loaded_model.predict([input_list])
    
    if pred[0] == 0:
        return 'Loan not sanctioned'
    else:
        return 'Loan sanctioned'