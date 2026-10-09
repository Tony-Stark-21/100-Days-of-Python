import requests
import os
from datetime import datetime
from dotenv import load_dotenv  # 1. Import dotenv

# 2. Load the variables from the .env file
load_dotenv()

nutrition_url = "https://app.100daysofpython.dev"
today = datetime.now()

# 3. Read variables directly from environment memory
headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY"),
    "Content-Type": "application/json"
}

post_url = f"{nutrition_url}/v1/nutrition/natural/exercise"
post_requirements = {
    "query": input("What exercise did you do today? "),
}

post_response = requests.post(post_url, json=post_requirements, headers=headers)
exercise = post_response.json()
first_exercise = exercise["exercises"][0]

sheet1 = {
    "sheet1": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": first_exercise["user_input"],
        "duration": first_exercise["duration_min"],
        "calories": first_exercise["nf_calories"],
    }
}


# 4. Removed headers=headers from this request because Sheety doesn't need Nutritionix keys
sheety_url = "https://api.sheety.co/e7084c9eef590c03d918f1d7288c38a4/myWorkouts/sheet1"
response = requests.post(
    url=sheety_url,
    json=sheet1,
    auth=(os.environ.get("SHEETY_USERNAME"),os.environ.get("SHEETY_PASSWORD")),
)
print(response.text)
