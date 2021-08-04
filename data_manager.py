
import requests
FLIGHT_DATA_ENDPOINT = "https://api.sheety.co/91fd50510c8320842d8851c13cbed29d/flightDeals/prices"
AUTHORIZATION_HEADERS = {
    "Authorization": "Bearer hackalert"
  }


# This class is responsible for talking to the Google Sheet.

class DataManager:

    def __init__(self):
        self.destination_data = {}

    # 2. Use the Sheety API to GET all the data in that sheet and print it out.
    def get_destination_data(self):
        sheet_response = requests.get(FLIGHT_DATA_ENDPOINT, headers=AUTHORIZATION_HEADERS)
        # print(sheet_response.status_code)     #prints 200 if API requests is successful
        data = sheet_response.json()
        self.destination_data = data["prices"]
        return self.destination_data








