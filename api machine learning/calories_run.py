import requests

url = "http://127.0.0.1:8000/cal_prediction"

input_data_for_model = {
    'Gender': 1,
    'Age': 36,
    'Height': 151.0,
    'Weight': 50.0,
    'Duration': 23.0,
    'Heart_Rate': 96.0,
    'Body_Temp': 40.7
    }

response = requests.post(url, json=input_data_for_model)
print(response.text)
