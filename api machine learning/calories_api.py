# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:49:49 2024

@author: ayush
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class CalorieInput(BaseModel):
    age: int
    weight: float
    height: float
    duration: float
    heart_rate: int
    body_temp: float

# Load the pre-trained model
calorie_model = pickle.load(open('D:/anaconda/calorie_model.sav', 'rb'))

@app.post('/calorie_prediction')
def calorie_pred(input_parameters: CalorieInput):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    input_list = [
        input_dictionary['age'],
        input_dictionary['weight'],
        input_dictionary['height'],
        input_dictionary['duration'],
        input_dictionary['heart_rate'],
        input_dictionary['body_temp']
    ]
    
    prediction = calorie_model.predict([input_list])
    
    return {"calories_burned": prediction[0]}
