import requests
import os
from flight_data import FlightData

TEQUILA_URL = "https://api.tequila.kiwi.com"
TEQUILA_API = os.environ.get("TEQUILA_API")

tequila_header = {
    "apikey": TEQUILA_API
}


class FlightSearch:

    def get_destination_code(self, city_name):
        tequila_iata_query = {
            "term": city_name
        }
        response = requests.get(url=f"{TEQUILA_URL}/locations/query", headers=tequila_header, params=tequila_iata_query)
        data = response.json()['locations']
        return data[0]['code']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_search_query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=tequila_header, params=flight_search_query)

        try:
            data = response.json()['data'][0]

        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]

        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
