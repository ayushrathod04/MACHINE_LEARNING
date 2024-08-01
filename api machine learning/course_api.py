from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    UserID: int
    CourseCategory: int
    TimeSpentOnCourse: float
    NumberOfVideosWatched: int
    NumberOfQuizzesTaken: int
    QuizScores: float
    CompletionRate: float
    DeviceType: int
    
onc_model = pickle.load(open('course_model.sav', 'rb'))

@app.post('/course_prediction')

def course_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    UserID = input_dictionary['UserID']
    CourseCategory = input_dictionary['CourseCategory']
    TimeSpentOnCourse = input_dictionary['TimeSpentOnCourse']
    NumberOfVideosWatched = input_dictionary['NumberOfVideosWatched']
    NumberOfQuizzesTaken = input_dictionary['NumberOfQuizzesTaken']
    QuizScores= input_dictionary['QuizScores']
    CompletionRate = input_dictionary['CompletionRate']
    DeviceType = input_dictionary['DeviceType']
    
    
    input_list=[UserID,CourseCategory,TimeSpentOnCourse,NumberOfVideosWatched,NumberOfQuizzesTaken,QuizScores,CompletionRate,DeviceType]
    
    prediction=onc_model.predict([input_list])
    if(prediction[0]==0):
        return 'The person has not completed course'
    else:
        return 'The person has completed course'