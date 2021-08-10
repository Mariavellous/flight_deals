# This class is responsible for talking to the Flight Search API.
import requests
TEQUILA_API_KEY = "Jb4o_zhT1mu6JEaY8Z8ZWDgVADWHjV1W"
class FlightSearch:
  def __init__(self):
    pass

  # For now, the FlightSearch class can respond with "TESTING" instead of IATA code
  def get_iata_code(self, city):
    location_query_endpoint = "https://tequila-api.kiwi.com/locations/query"
    headers = {"apikey": TEQUILA_API_KEY}
    city_params = {
      "term": city,
      "location_types": "airport",
    }
    response = requests.get(url=location_query_endpoint, params=city_params, headers=headers)
    data = response.json()
    iata_code = data["locations"][0]["id"]
    return iata_code

