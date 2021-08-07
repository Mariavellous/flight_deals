#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

# 4. Pass everything stored in the "prices" (sheet name) key back to the main.py file and
# store it in a variable called sheet_data, so that you can print the sheet_data from main.py
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

flight_search = FlightSearch()

# Check to see if sheet_data has any values for "iataCode" key
for city in sheet_data:
  # if IATA Codes is empty
  if city["iataCode"] == "":
    # Pass each city name in sheet_data one-by-one to the FlightSearch class.
    city_name = city["city"]
    # Use the response from the FlightSearch class to update the sheet_data
    city["iataCode"] = flight_search.get_iata_code(city_name) # "TESTING"

  data_manager.get_destination_data = sheet_data
  data_manager.update_iata_code()
  # print(sheet_data)

