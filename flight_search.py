# This class is responsible for talking to the Flight Search API.
import requests

class FlightSearch:
  def __init__(self):
    pass

  # For now, the FlightSearch class can respond with "TESTING" instead of IATA code
  def get_iata_code(self, city):
    kiwi_url = "https://tequila-api.kiwi.com/locations/query"
    headers = {"apikey": "Jb4o_zhT1mu6JEaY8Z8ZWDgVADWHjV1W"}
    city_params = {
      "term": city,
      "location_types": "airport",
    }
    response = requests.get(url=kiwi_url, params=city_params, headers=headers)
    data = response.json()
    iata_code = data["locations"][0]["id"]
    return iata_code

