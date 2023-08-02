import requests
import os

SHEET_URL = "https://api.sheety.co/5fe6747dbbfc9cf7184f6239e652cfc4/flightDeals/prices"
SHEET_API_KEY = os.environ.get("SHEET_API_KEY")

sheet_header = {
    "Authorization": SHEET_API_KEY
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_URL, headers=sheet_header)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_URL}/{city['id']}",
                json=new_data
            )
            # print(response.text)
