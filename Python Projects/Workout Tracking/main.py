import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 79
HEIGHT_CM = 173
AGE = 30

API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
SHEET_TOKEN = os.environ.get("BEARER_TOKEN")

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/5fe6747dbbfc9cf7184f6239e652cfc4/myWorkouts/workouts"

workout_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": workout_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

sheet_header = {
    "Authorization": SHEET_TOKEN
}
response = requests.post(url=NUTRITIONIX_URL, headers=headers, json=exercise_params)
response.raise_for_status()
results = response.json()

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%X")

for exercise in results["exercises"]:
    sheet_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }

    }
    sheet_response = requests.post(url=SHEET_URL, json=sheet_params, headers=sheet_header)

    print(sheet_response.text)
