# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:00:25 2024

@author: ayush
"""

#calorie_prediction#
import json
import requests

url = "http://127.0.0.1:8000/calorie_prediction"

input_data_for_model = {
    "age": 25,
    "weight": 70.5,
    "height": 175.0,
    "duration": 30.0,
    "heart_rate": 120,
    "body_temp": 36.6
}

    

input_json=json.dumps(input_data_for_model)

response=requests.post(url,data=input_json)
print(response.text)