# 1. Import Necessary Libraries 
from fastapi import FastAPI 
from pydantic import BaseModel 
import pickle 

# 2. Create a FastAPI App 
app = FastAPI() 

# 3. Define a Pydantic Model 

class ModelInput(BaseModel): 
	Pregnancies: int
	Glucose: int
	BloodPressure: int
	SkinThickness: int
	Insulin: int
	BMI: float
	DiabetesPedigreeFunction: float
	Age: int


# 4. Load a Pre-trained Machine Learning Model 
with open('D:/anaconda/trained_model.sav', 'rb') as model_file: 
	diabetes_model = pickle.load(model_file) 

# 5. Define a POST Endpoint for Diabetes Prediction 

@app.post('/diabetes_prediction') 
def diabetes_pred(input_parameters: ModelInput): 
	preg, glu, bp, skin, insulin, bmi, dpf, age = ( 
		input_parameters.Pregnancies, input_parameters.Glucose, 
		input_parameters.BloodPressure, input_parameters.SkinThickness, 
		input_parameters.Insulin, input_parameters.BMI, 
		input_parameters.DiabetesPedigreeFunction, input_parameters.Age 
	) 

	input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age] 

	prediction = diabetes_model.predict([input_list]) 

	if prediction[0] == 0: 
		return 'The Person is not Diabetic'
	else: 
		return 'The person is Diabetic'
