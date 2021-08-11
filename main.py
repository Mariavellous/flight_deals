#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# 4. Pass everything stored in the "prices" (sheet name) key back to the main.py file and
# store it in a variable called sheet_data, so that you can print the sheet_data from main.py
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

flight_search = FlightSearch()
flight_data = FlightData()


# Check to see if sheet_data has any values for "iataCode" key
for city in sheet_data:
  # if IATA Codes is empty
  if city["iataCode"] == "":
    # Pass each city name in sheet_data one-by-one to the FlightSearch class.
    city_name = city["city"]
    # {'locations': [{'id': 'CDG', 'int_id': 9667, 'airport_int_id': 9667, 'active': True, 'code': 'CDG', 'icao': 'LFPG', 'name': 'Charles de Gaulle Airport', 'slug': 'charles-de-gaulle-paris-france', 'slug_en': 'charles-de-gaulle-paris-france', 'alternative_names': ['Aéroport de Paris-Charles-de-Gaulle', 'Paris (CDG)'], 'rank': 31, 'global_rank_dst': 14, 'dst_popularity_score': 1427536.0, 'timezone': 'Europe/Paris', 'city': {'id': 'paris_fr', 'name': 'Paris', 'code': 'PAR', 'slug': 'paris-france', 'region': {'id': 'western-europe', 'name': 'Western Europe', 'slug': 'western-europe'}, 'subdivision': None, 'continent': {'id': 'europe', 'name': 'Europe', 'slug': 'europe', 'code': 'EU'}, 'autonomous_territory': None, 'country': {'id': 'FR', 'name': 'France', 'slug': 'france', 'code': 'FR'}}, 'location': {'lat': 49.009722, 'lon': 2.547778}, 'alternative_departure_points': [{'id': 'LBG', 'distance': 14.56, 'duration': 1359}, {'id': 'FR-PLAI-PARC', 'distance': 16.69, 'duration': 796}, {'id': 'FR-PARI-PA14', 'distance': 22.2, 'duration': 1160.5}, {'id': 'FR-PARI-PA10', 'distance': 22.52, 'duration': 1236.7}, {'id': 'FR-PARI-PAR7', 'distance': 25.31, 'duration': 1432}, {'id': 'FR-PARI-PA12', 'distance': 25.64, 'duration': 1478}, {'id': 'FR-PARI-PAR9', 'distance': 27.21, 'duration': 1569.5}, {'id': 'FR-PARI-PAR3', 'distance': 27.37, 'duration': 1497.7}, {'id': 'FR-PARI-PA11', 'distance': 27.6, 'duration': 1586.1}, {'id': 'FR-PARI-PARI', 'distance': 28.62, 'duration': 1581.7}, {'id': 'FR-PARI-PA13', 'distance': 29.07, 'duration': 1604.6}, {'id': 'FR-PARI-PLAC', 'distance': 29.6, 'duration': 1765.5}, {'id': 'FR-PARI-PAR1', 'distance': 30.33, 'duration': 1711.6}, {'id': 'FR-PARI-PAR2', 'distance': 30.48, 'duration': 1747}, {'id': 'FR-DISN-PARI', 'distance': 41.46, 'duration': 2213.1}, {'id': 'ORY', 'distance': 44.54, 'duration': 2554.2}, {'id': 'XJY', 'distance': 45.49, 'duration': 2562.7}, {'id': 'BVA', 'distance': 78.32, 'duration': 3340.6}, {'id': 'LIL', 'distance': 190.06, 'duration': 7266.3}, {'id': 'XCR', 'distance': 198.74, 'duration': 8435.4}, {'id': 'DOL', 'distance': 213.47, 'duration': 8513.2}], 'tags': [{'tag': 'sightseeing', 'month_to': -1, 'month_from': -1}, {'tag': 'culture', 'month_to': -1, 'month_from': -1}, {'tag': 'famous cities', 'month_to': -1, 'month_from': -1}, {'tag': 'romance', 'month_to': -1, 'month_from': -1}, {'tag': 'city break', 'month_to': -1, 'month_from': -1}], 'providers': [1028, 1035, 1053, 1064, 1096, 1128, 1148, 1163, 1175, 1227, 1229, 1283, 1291, 1329], 'special': [{'id': 'notre-dame_poi', 'name': 'Notre Dame', 'slug': 'notre-dame'}, {'id': 'eiffel-tower_poi', 'name': 'Eiffel Tower', 'slug': 'eiffel-tower'}, {'id': 'louvre-museum_poi', 'name': 'Louvre Museum', 'slug': 'louvre-museum'}, {'id': 'versailles_poi', 'name': 'Versailles', 'slug': 'versailles'}, {'id': 'giverny_poi', 'name': 'Giverny', 'slug': 'giverny'}, {'id': 'le-cimetiere-de-pere-lachaise_poi', 'name': 'Le Cimetiere de Pere Lachaise', 'slug': 'le-cimetiere-de-pere-lachaise'}], 'tourist_region': [{'id': 'ile-de-france_poi', 'name': 'Ile de France', 'slug': 'ile-de-france'}, {'id': 'greater-paris_poi', 'name': 'Greater Paris', 'slug': 'greater-paris'}, {'id': 'autoroute-utrecht-paris_poi', 'name': 'Autoroute Utrecht Paris', 'slug': 'autoroute-utrecht-paris'}], 'car_rentals': [{'provider_id': 1175, 'providers_locations': ['644548']}], 'new_ground': False, 'routing_priority': 0, 'type': 'airport'}, {'id': 'ORY', 'int_id': 2684, 'airport_int_id': 2684, 'active': True, 'code': 'ORY', 'icao': 'LFPO', 'name': 'Paris Orly', 'slug': 'paris-orly-paris-france', 'slug_en': 'paris-orly-paris-france', 'alternative_names': ['Aéroport de Paris-Orly', 'Paris Orly (ORLY 2)'], 'rank': 34, 'global_rank_dst': 34, 'dst_popularity_score': 549226.0, 'timezone': 'Europe/Paris', 'city': {'id': 'paris_fr', 'name': 'Paris', 'code': 'PAR', 'slug': 'paris-france', 'region': {'id': 'western-europe', 'name': 'Western Europe', 'slug': 'western-europe'}, 'subdivision': None, 'continent': {'id': 'europe', 'name': 'Europe', 'slug': 'europe', 'code': 'EU'}, 'autonomous_territory': None, 'country': {'id': 'FR', 'name': 'France', 'slug': 'france', 'code': 'FR'}}, 'location': {'lat': 48.723333, 'lon': 2.379444}, 'alternative_departure_points': [{'id': 'XJY', 'distance': 13.15, 'duration': 1045.1}, {'id': 'FR-PARI-PLAC', 'distance': 16.47, 'duration': 1185.9}, {'id': 'FR-PARI-PA13', 'distance': 18.13, 'duration': 1241.2}, {'id': 'FR-PARI-PARI', 'distance': 18.56, 'duration': 1273.7}, {'id': 'FR-PARI-PA11', 'distance': 19.34, 'duration': 1377.2}, {'id': 'FR-PARI-PAR1', 'distance': 20.27, 'duration': 1403.6}, {'id': 'FR-PARI-PA12', 'distance': 22.73, 'duration': 1655.9}, {'id': 'FR-PARI-PA14', 'distance': 23.46, 'duration': 1608.9}, {'id': 'FR-ARPA-BUSS', 'distance': 25.11, 'duration': 1774.2}, {'id': 'FR-PARI-PAR3', 'distance': 26.73, 'duration': 1802.8}, {'id': 'FR-PARI-PAR9', 'distance': 29.73, 'duration': 2022.5}, {'id': 'FR-PARI-PAR2', 'distance': 29.97, 'duration': 2007.1}, {'id': 'FR-PARI-PAR7', 'distance': 30.02, 'duration': 2042.5}, {'id': 'FR-PARI-PA10', 'distance': 31.05, 'duration': 2080.5}, {'id': 'LBG', 'distance': 43.5, 'duration': 3051.7}, {'id': 'CDG', 'distance': 46.17, 'duration': 2586.4}, {'id': 'BVA', 'distance': 103.43, 'duration': 5376}, {'id': 'XCR', 'distance': 162.48, 'duration': 8598.9}, {'id': 'DOL', 'distance': 211.42, 'duration': 8669.3}, {'id': 'TUF', 'distance': 227.6, 'duration': 8703.3}, {'id': 'LIL', 'distance': 232.53, 'duration': 9528.8}], 'tags': [{'tag': 'sightseeing', 'month_to': -1, 'month_from': -1}, {'tag': 'culture', 'month_to': -1, 'month_from': -1}, {'tag': 'famous cities', 'month_to': -1, 'month_from': -1}, {'tag': 'romance', 'month_to': -1, 'month_from': -1}, {'tag': 'city break', 'month_to': -1, 'month_from': -1}], 'providers': [1035, 1096, 1148, 1227, 1229, 1283, 1291, 1329], 'special': [{'id': 'chateau-de-chenonceau_poi', 'name': 'Chateau de Chenonceau', 'slug': 'chateau-de-chenonceau'}, {'id': 'le-cimetiere-de-pere-lachaise_poi', 'name': 'Le Cimetiere de Pere Lachaise', 'slug': 'le-cimetiere-de-pere-lachaise'}, {'id': 'giverny_poi', 'name': 'Giverny', 'slug': 'giverny'}, {'id': 'louvre-museum_poi', 'name': 'Louvre Museum', 'slug': 'louvre-museum'}, {'id': 'versailles_poi', 'name': 'Versailles', 'slug': 'versailles'}, {'id': 'notre-dame_poi', 'name': 'Notre Dame', 'slug': 'notre-dame'}, {'id': 'eiffel-tower_poi', 'name': 'Eiffel Tower', 'slug': 'eiffel-tower'}], 'tourist_region': [{'id': 'ile-de-france_poi', 'name': 'Ile de France', 'slug': 'ile-de-france'}, {'id': 'greater-paris_poi', 'name': 'Greater Paris', 'slug': 'greater-paris'}, {'id': 'autoroute-utrecht-paris_poi', 'name': 'Autoroute Utrecht Paris', 'slug': 'autoroute-utrecht-paris'}], 'car_rentals': [], 'new_ground': False, 'routing_priority': 0, 'type': 'airport'}, {'id': 'BVA', 'int_id': 7346, 'airport_int_id': 7346, 'active': True, 'code': 'BVA', 'icao': 'LFOB', 'name': 'Beauvais–Tillé', 'slug': 'beauvais-tille-paris-france', 'slug_en': 'beauvais-tille-paris-france', 'alternative_names': ['Aéroport de Paris-Beauvais'], 'rank': 74, 'global_rank_dst': 145, 'dst_popularity_score': 83630.0, 'timezone': 'Europe/Paris', 'city': {'id': 'paris_fr', 'name': 'Paris', 'code': 'PAR', 'slug': 'paris-france', 'region': {'id': 'western-europe', 'name': 'Western Europe', 'slug': 'western-europe'}, 'subdivision': None, 'continent': {'id': 'europe', 'name': 'Europe', 'slug': 'europe', 'code': 'EU'}, 'autonomous_territory': None, 'country': {'id': 'FR', 'name': 'France', 'slug': 'france', 'code': 'FR'}}, 'location': {'lat': 49.454444, 'lon': 2.112778}, 'alternative_departure_points': [{'id': 'CDG', 'distance': 78.17, 'duration': 3313.4}, {'id': 'LBG', 'distance': 81.63, 'duration': 3970.1}, {'id': 'ORY', 'distance': 103.94, 'duration': 5411.8}, {'id': 'DOL', 'distance': 170.78, 'duration': 8737.6}, {'id': 'LIL', 'distance': 188.92, 'duration': 7522.9}, {'id': 'CFR', 'distance': 221.31, 'duration': 10639.3}, {'id': 'XCR', 'distance': 230.06, 'duration': 11133}], 'tags': [{'tag': 'sightseeing', 'month_to': -1, 'month_from': -1}, {'tag': 'culture', 'month_to': -1, 'month_from': -1}, {'tag': 'famous cities', 'month_to': -1, 'month_from': -1}, {'tag': 'romance', 'month_to': -1, 'month_from': -1}, {'tag': 'city break', 'month_to': -1, 'month_from': -1}], 'providers': [1035, 1148, 1175, 1229, 1283, 1329], 'special': [{'id': 'louvre-museum_poi', 'name': 'Louvre Museum', 'slug': 'louvre-museum'}, {'id': 'notre-dame_poi', 'name': 'Notre Dame', 'slug': 'notre-dame'}, {'id': 'giverny_poi', 'name': 'Giverny', 'slug': 'giverny'}, {'id': 'le-cimetiere-de-pere-lachaise_poi', 'name': 'Le Cimetiere de Pere Lachaise', 'slug': 'le-cimetiere-de-pere-lachaise'}, {'id': 'versailles_poi', 'name': 'Versailles', 'slug': 'versailles'}, {'id': 'eiffel-tower_poi', 'name': 'Eiffel Tower', 'slug': 'eiffel-tower'}], 'tourist_region': [{'id': 'ile-de-france_poi', 'name': 'Ile de France', 'slug': 'ile-de-france'}, {'id': 'greater-paris_poi', 'name': 'Greater Paris', 'slug': 'greater-paris'}, {'id': 'autoroute-utrecht-paris_poi', 'name': 'Autoroute Utrecht Paris', 'slug': 'autoroute-utrecht-paris'}], 'car_rentals': [{'provider_id': 1175, 'providers_locations': ['479433']}], 'new_ground': False, 'routing_priority': 0, 'type': 'airport'}, {'id': 'PAS', 'int_id': 2848, 'airport_int_id': 2848, 'active': True, 'code': 'PAS', 'icao': 'LGPA', 'name': 'Paros National', 'slug': 'paros-national-parikia-greece', 'slug_en': 'paros-national-parikia-greece', 'alternative_names': ['Κρατικός Αερολιμένας Πάρου'], 'rank': 320, 'global_rank_dst': 197, 'dst_popularity_score': 81119.0, 'timezone': 'Europe/Athens', 'city': {'id': 'parikia_gr', 'name': 'Parikia', 'code': 'PAS', 'slug': 'parikia-greece', 'region': {'id': 'southern-europe', 'name': 'Southern Europe', 'slug': 'southern-europe'}, 'subdivision': None, 'continent': {'id': 'europe', 'name': 'Europe', 'slug': 'europe', 'code': 'EU'}, 'autonomous_territory': None, 'country': {'id': 'GR', 'name': 'Greece', 'slug': 'greece', 'code': 'GR'}}, 'location': {'lat': 37.010278, 'lon': 25.128611}, 'alternative_departure_points': [{'id': 'JNX', 'distance': 46.32, 'duration': 23526.3}, {'id': 'JSY', 'distance': 60.16, 'duration': 33952.3}, {'id': 'JMK', 'distance': 65.76, 'duration': 36477.7}, {'id': 'JTR', 'distance': 127.0, 'duration': 76848.8}, {'id': 'MLO', 'distance': 169.52, 'duration': 58512.6}, {'id': 'JIK', 'distance': 180.2, 'duration': 96937.1}, {'id': 'JKL', 'distance': 200.5, 'duration': 132885.5}, {'id': 'LRS', 'distance': 215.43, 'duration': 140771.3}, {'id': 'KGS', 'distance': 217.59, 'duration': 142978.6}, {'id': 'JTY', 'distance': 226.63, 'duration': 152170.6}, {'id': 'ATH', 'distance': 232.38, 'duration': 46907.4}], 'tags': [{'tag': 'beach', 'month_to': -1, 'month_from': -1}, {'tag': 'nightlife', 'month_to': -1, 'month_from': -1}], 'providers': [1175], 'special': [], 'tourist_region': [{'id': 'south-aegean_poi', 'name': 'South Aegean', 'slug': 'south-aegean'}, {'id': 'autumn-sun_poi', 'name': 'Autumn Sun', 'slug': 'autumn-sun'}, {'id': 'cyclades_poi', 'name': 'Cyclades', 'slug': 'cyclades'}, {'id': 'greek-islands_poi', 'name': 'Greek Islands', 'slug': 'greek-islands'}, {'id': 'mediterranean_poi', 'name': 'Mediterranean', 'slug': 'mediterranean'}, {'id': 'paros_poi', 'name': 'Paros', 'slug': 'paros'}], 'car_rentals': [{'provider_id': 1175, 'providers_locations': ['4146883']}], 'new_ground': False, 'routing_priority': 0, 'type': 'airport'}, {'id': 'TMU', 'int_id': 4174, 'airport_int_id': 4174, 'active': True, 'code': 'TMU', 'icao': 'MRTR', 'name': 'Tambor', 'slug': 'tambor-tambor-costa-rica', 'slug_en': 'tambor-tambor-costa-rica', 'alternative_names': ['Aeropuerto Tambor', 'Santa Teresa', 'Mal País'], 'rank': 220, 'global_rank_dst': 576, 'dst_popularity_score': 5806.0, 'timezone': 'America/Costa_Rica', 'city': {'id': 'tambor_cr', 'name': 'Tambor', 'code': 'TMU', 'slug': 'tambor-costa-rica', 'region': {'id': 'central-america', 'name': 'Central America', 'slug': 'central-america'}, 'subdivision': None, 'continent': {'id': 'north-america', 'name': 'North America', 'slug': 'north-america', 'code': 'NA'}, 'autonomous_territory': None, 'country': {'id': 'CR', 'name': 'Costa Rica', 'slug': 'costa-rica', 'code': 'CR'}}, 'location': {'lat': 9.739722, 'lon': -85.016944}, 'alternative_departure_points': [{'id': 'SJO', 'distance': 123.07, 'duration': 12792.3}, {'id': 'NOB', 'distance': 124.5, 'duration': 9893.9}, {'id': 'FON', 'distance': 144.14, 'duration': 13584.5}, {'id': 'TNO', 'distance': 162.17, 'duration': 11490.5}, {'id': 'LIR', 'distance': 173.39, 'duration': 11607.3}, {'id': 'XQP', 'distance': 180.83, 'duration': 17161.9}], 'tags': [{'tag': 'diving&snorkeling', 'month_to': -1, 'month_from': -1}, {'tag': 'beach', 'month_to': -1, 'month_from': -1}], 'providers': [1175, 1282], 'special': [], 'tourist_region': [], 'car_rentals': [{'provider_id': 1175, 'providers_locations': ['1411486']}], 'new_ground': False, 'routing_priority': 0, 'type': 'airport'}, {'id': 'PRN', 'int_id': 3384, 'airport_int_id': 3384, 'active': True, 'code': 'PRN', 'icao': 'BKPR', 'name': 'Pristina International', 'slug': 'pristina-international-pristina-kosovo', 'slug_en': 'pristina-international-pristina-kosovo', 'alternative_names': [], 'rank': 150, 'global_rank_dst': 68, 'dst_popularity_score': 373170.0, 'timezone': 'Europe/Belgrade', 'city': {'id': 'pristina_xk', 'name': 'Pristina', 'code': 'PRN', 'slug': 'pristina-kosovo', 'region': {'id': 'southern-europe', 'name': 'Southern Europe', 'slug': 'southern-europe'}, 'subdivision': None, 'continent': {'id': 'europe', 'name': 'Europe', 'slug': 'europe', 'code': 'EU'}, 'autonomous_territory': None, 'country': {'id': 'XK', 'name': 'Kosovo', 'slug': 'kosovo', 'code': 'XK'}}, 'location': {'lat': 42.572778, 'lon': 21.035833}, 'alternative_departure_points': [{'id': 'SKP', 'distance': 118.33, 'duration': 5351.6}, {'id': 'INI', 'distance': 142.86, 'duration': 8752.1}, {'id': 'KVO', 'distance': 217.51, 'duration': 13303.9}, {'id': 'TIA', 'distance': 227.34, 'duration': 11305.2}, {'id': 'OHD', 'distance': 248.41, 'duration': 13384}], 'tags': [{'tag': 'sightseeing', 'month_to': -1, 'month_from': -1}], 'providers': [1175, 1283], 'special': [], 'tourist_region': [], 'car_rentals': [{'provider_id': 1175, 'providers_locations': ['925408']}], 'new_ground': False, 'routing_priority': 0, 'type': 'airport'}, {'id': 'PIN', 'int_id': 4272, 'airport_int_id': 4272, 'active': True, 'code': 'PIN', 'icao': 'SWPI', 'name': 'Parintins', 'slug': 'parintins-parintins-state-of-amazonas-brazil', 'slug_en': 'parintins-parintins-state-of-amazonas-brazil', 'alternative_names': ['Aeroporto Júlio Belém'], 'rank': 1802, 'global_rank_dst': 838, 'dst_popularity_score': 1914.0, 'timezone': 'America/Manaus', 'city': {'id': 'parintins_am_br', 'name': 'Parintins', 'code': 'PIN', 'slug': 'parintins-state-of-amazonas-brazil', 'region': {'id': 'southern-america', 'name': 'Southern America', 'slug': 'southern-america'}, 'subdivision': {'id': 'AM_BR', 'name': 'State of Amazonas', 'slug': 'state-of-amazonas-brazil', 'code': 'AM'}, 'continent': {'id': 'south-america', 'name': 'South America', 'slug': 'south-america', 'code': 'SA'}, 'autonomous_territory': None, 'country': {'id': 'BR', 'name': 'Brazil', 'slug': 'brazil', 'code': 'BR'}}, 'location': {'lat': -2.673889, 'lon': -56.778056}, 'alternative_departure_points': [], 'tags': [{'tag': 'events', 'month_to': -1, 'month_from': -1}], 'providers': [1277, 1282], 'special': [], 'tourist_region': [], 'car_rentals': [], 'new_ground': False, 'routing_priority': 0, 'type': 'airport'}], 'meta': {'locale': {'code': 'en-US', 'status': 'Locale not specified, using default.'}}, 'last_refresh': 1628256540, 'results_retrieved': 7}
    # Use the response from the FlightSearch class to update the sheet_data
    city["iataCode"] = flight_search.get_iata_code(city_name) # "TESTING"


data_manager.update_iata_code()
#print(sheet_data)

# Search for flight prices in GBP from London(LON) to all destinations in the google sheet
for city in sheet_data:
  city_name = city["city"]
  city_iata_code = city["iataCode"]
  price = flight_data.get_flight_price(city_iata_code)
  print(f"{city_name}: £{price}")

  # if price is lower than lowestPrice set on google sheet, send text notification of the flight
  if price < city["lowestPrice"]:
    departure_city = flight_data.departure_city
    departure_iata_code = flight_data.departure_airport_code
    departure_date = flight_data.outbound_date
    arrival_date = flight_data.inbound_date
    arrival_airport = flight_data.arrival_city_iata_code
    notification_manager = NotificationManager(departure_city, departure_iata_code, departure_date, arrival_date)
    notification_manager.send_price_alert(price, city_name, arrival_airport)

