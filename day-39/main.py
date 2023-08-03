from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
print(sheet_data)

ORIGIN_CITY_IATA = "BOS"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today)
    if destination["lowestPrice"] > flight.price:
        notification_manager.send_text(message=f"Low price alert! Only ${flight.price} to fly from "
                                               f"{flight.origin_city}-{flight.origin_airport}"
                                               f" to {flight.destination_city}-{flight.destination_airport},"
                                               f" from {flight.out_date} to {flight.return_date}.")
        # destination["lowestPrice"] = data_manager.update_lowest_price(flight.price)

