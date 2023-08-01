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
        self.destination_data = requests.get(url=SHEET_URL, headers=sheet_header)
        return self.destination_data.json()['prices']

