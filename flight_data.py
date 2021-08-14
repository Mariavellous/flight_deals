from datetime import datetime
from datetime import timedelta
import requests

TEQUILA_API_KEY = "Jb4o_zhT1mu6JEaY8Z8ZWDgVADWHjV1W"
TEQUILA_ENDPOINT = "https:tequila-api.kiwi.com/"

today = datetime.today()
# Use Timedelta to specify how many (days, hours, min)
add_1_day = timedelta(days=1)
add_180_days = timedelta(days=180)

# Find out what tomorrow's date is in this specific format
TOMORROW = (today + add_1_day).strftime("%m/%d/%Y")
# Find out what 6 months from today's date in this specific format
DAY_180 = (today + add_180_days).strftime("%m/%d/%Y")

# This class is responsible for structuring the flight data.
class FlightData:
  def __init__(self):
    self.departure_airport_code = "LON"
    self.departure_city = "London"
    self.arrival_city = ""
    self.arrival_city_iata_code = ""
    self.outbound_date = ""
    self.inbound_date = ""

# Use Tequila/Kiwi API to retrieve flight prices (params = personalized)
# This returns the price of the first available flight with given params.
# iata_code is passed on here
  def get_flight_price(self, iata_code):
    flight_endpoint = "https://tequila-api.kiwi.com/search"
    headers = {"apikey": TEQUILA_API_KEY}
    params = {
      "fly_from": self.departure_airport_code,
      "fly_to": iata_code,
      "data_from": TOMORROW,
      "date_to": DAY_180,
      "nights_in_dst_from": 7,
      "nights_in_dst_to": 28,
      "flight_type": "round",
      "adults": 1,
      "curr": "GBP",
      "max_stopovers": 0,
      "conn_on_diff_airport": 0
    }
    response = requests.get(url=flight_endpoint, params=params, headers=headers)
    # This data contains ALL the flight searches

    data = response.json()

    # print(response.text)
    # Extract the departure date of the flight search at index 0
    try:
      departure_date = data["data"][0]["route"][0]["dTime"]  # result in unix time or epoch time
    except:
      print("There is no direct flight.")
      return None

    # Convert the unix time into readable date
    date_of_departure = datetime.fromtimestamp(departure_date).strftime("%Y-%m-%d")
    # Set the date_of_departure as a FlightData attribute
    self.outbound_date = date_of_departure
    # Extract the arrival date of the flight search at index 0
    arrival_date = data["data"][0]["route"][1]["aTime"]  # result in unix time or epoch time
    # Convert the unix time into readable date
    date_of_arrival = datetime.fromtimestamp(arrival_date).strftime("%Y-%m-%d")
    # Set the date_of_arrival as a FlightData attribute
    self.inbound_date = date_of_arrival
    # Set the arrival_city_iata_code as a FlightData attribute
    self.arrival_city_iata_code = data["data"][0]["flyTo"]
    # Extract the flight price of the flight search at index 0
    flight_price = data["data"][0]["price"]
    return flight_price
