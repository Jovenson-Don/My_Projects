import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "joeydon21@gmail.com"
MY_PASSWORD = "hsrlelkbiiaihwgg"

MY_LAT = 42.083302
MY_LONG = -71.019897
COORDINATATION = (MY_LAT, MY_LONG)


def check_coordinatation():
    if 5 >= iss_latitude % MY_LAT > 0 or 5 >= MY_LAT % iss_latitude > 0 and \
            -5 <= iss_longitude % MY_LONG > 0 or -5 <= MY_LONG % iss_longitude < 0:
        return True


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_coordination = (iss_longitude, iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

while True:
    time.sleep(60)
    if check_coordinatation() is True and time_now >= sunset or time_now <= sunset:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:Look up!\n\n Look up now before its too late!")
