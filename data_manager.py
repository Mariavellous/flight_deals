
import requests
FLIGHT_DATA_ENDPOINT = "https://api.sheety.co/42f814c3ae031eff9e1a02361d092390/flightDeals/prices"
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

    def update_iata_code(self):
        for city in self.destination_data:
            object_id = city["id"]
            update_url = f"https://api.sheety.co/42f814c3ae031eff9e1a02361d092390/flightDeals/prices/{object_id}"
            params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=update_url, json=params, headers=AUTHORIZATION_HEADERS)
            # print(response.status_code)








