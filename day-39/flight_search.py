import requests
import os

TEQUILA_URL = "https://api.tequila.kiwi.com"
TEQUILA_API = os.environ.get("TEQUILA_API")


class FlightSearch:

    def get_destination_code(self, city_name):
        tequila_header = {
            "apikey": TEQUILA_API
        }

        tequila_parameter = {
            "term": city_name
        }
        response = requests.get(url=f"{TEQUILA_URL}/locations/query", headers=tequila_header, params=tequila_parameter)
        data = response.json()['locations']
        return data[0]['code']
