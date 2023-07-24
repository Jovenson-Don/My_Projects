import requests
import os
from twilio.rest import Client

weather_api = "https://api.openweathermap.org/data/2.8/onecall"
api_key = os.environ.get("OWM_API_KEY")
MY_LAT = 42.083302
MY_LONG = -71.019897
account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "minutely,current,daily",

}

response = requests.get(url=weather_api, params=weather_params)
response.raise_for_status()

weather_data = response.json()
hourly_weather = (weather_data["hourly"][:12])

will_rain = False

for hour_data in hourly_weather:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

client = Client(account_sid, auth_token)
if will_rain:
    message = client.messages.create(body="It's going to rain today. Bring umbrella!",
                                     from_='+18665083998', to='+17742402535')
    print(message.sid)
else:
    message = client.messages.create(body="No rain today. You good!",
                                     from_='+18665083998', to='+17742402535')
    print(message.sid)
