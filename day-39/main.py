from pprint import pprint
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

for n in range(len(sheet_data)):
    if sheet_data[n]["iataCode"] == "":
        pass
