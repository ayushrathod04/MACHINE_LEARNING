

import json
import requests

url = 'http://127.0.0.1:8000/loan_prediction'

input_data_for_model = {
    'Gender' : 0,
    'Married' : 1,
    'Dependents' : 0,
    'Education' : 1,
    'Self_Employed' : 1,
    'ApplicantIncome' : 3000,
    'CoapplicantIncome' : 0.0,
    'LoanAmount' : 66.0,
    'Loan_Amount_Term' : 360.0,
    'Credit_History' : 1.0,
    'Property_Area' : 2
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url,data=input_json)

print(response.text)