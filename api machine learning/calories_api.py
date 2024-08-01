from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    Gender: int
    Age: int  # Corrected field name to lowercase
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float
    
cal_loaded_model = pickle.load(open('D:/anaconda/calorie_model.sav', 'rb'))

@app.post('/cal_prediction')
def hr_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    Gender = input_dictionary['Gender']
    Age = input_dictionary['Age']  # Corrected field name to lowercase
    Height = input_dictionary['Height']
    Weight = input_dictionary['Weight']
    Duration = input_dictionary['Duration']
    Heart_Rate = input_dictionary['Heart_Rate']
    Body_Temp= input_dictionary['Body_Temp']
   
    
    
    input_list=[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]
    
    prediction=cal_loaded_model.predict([input_list])
    return prediction
