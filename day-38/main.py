import requests
import os

GENDER = "male"
WEIGHT_KG = 79
HEIGHT_CM = 173
AGE = 30

API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

workout_text = input("Tell me which exercise you did: ")

exercise_params = {
    "query": workout_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=API_URL, headers=headers, json=exercise_params)
response.raise_for_status()
print(response.json())
