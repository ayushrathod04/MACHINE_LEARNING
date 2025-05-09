import json
import requests

url = "http://127.0.0.1:8000/heart_prediction"

input_data_for_model = {
    'age': 57,
    'sex': 0,
    'cp': 0,
    'trestbps': 120,
    'chol': 354,
    'fbs': 0,
    'restecg': 1,
    'thalach': 163,
    'exang': 1,
    'oldpeak': 0.6,
    'slope': 2,
    'ca': 0,
    'thal': 2
    }

input_json=json.dumps(input_data_for_model)

response=requests.post(url,data=input_json)
print(response.text)