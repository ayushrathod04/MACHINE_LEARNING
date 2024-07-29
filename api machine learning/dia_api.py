# Import the necessary libraries 
import json 
import requests 

# Define the URL of the diabetes prediction model 
url = 'http://127.0.0.1:8000/diabetes_prediction'

# Prepare input data for the model in a dictionary 
input_data_for_model = { 
	"Pregnancies": 6, 
	"Glucose": 148, 
	"BloodPressure": 72, 
	"SkinThickness": 35, 
	"Insulin": 0, 
	"BMI": 33.6, 
	"DiabetesPedigreeFunction": 0.627, 
	"Age": 50
} 

# Convert the input data dictionary to a JSON-formatted string 
input_json = json.dumps(input_data_for_model) 

# Send a POST request to the model's URL with the input JSON data 
response = requests.post(url, data=input_json) 

# Print the response received from the model 
print(response.text) 
