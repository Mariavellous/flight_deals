
import requests
FLIGHT_DATA_ENDPOINT = "https://api.sheety.co/91fd50510c8320842d8851c13cbed29d/flightDeals/prices"
AUTHORIZATION_HEADERS = {
    "Authorization": "Bearer hackalert"
  }


# This class is responsible for talking to the Google Sheet.

class DataManager:
    # 2. Use the Sheety API to GET all the data in that sheet and print it out.
    def destination_data(self):
        sheet_response = requests.get(FLIGHT_DATA_ENDPOINT, headers=AUTHORIZATION_HEADERS)
        print(sheet_response.status_code)
        data = sheet_response.json()
        return data


data_manager = DataManager()
data_manager.destination_data()
print(data_manager.destination_data())





