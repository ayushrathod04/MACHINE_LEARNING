import json
import requests

url = "https://65d5-34-145-70-111.ngrok-free.app/course_prediction"

input_data_for_model = {
    "UserID": 8650,
    "CourseCategory": 1,
    "TimeSpentOnCourse": 79.466129,
    "NumberOfVideosWatched": 12.000000,
    "NumberOfQuizzesTaken": 7.000000,
    "QuizScores": 70.233329,
    "CompletionRate": 76.484023,
    "DeviceType": 0.000000
}

input_json=json.dumps(input_data_for_model)

response=requests.post(url,data=input_json)
print(response.text)