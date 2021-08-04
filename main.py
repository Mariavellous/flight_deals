#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

# 4. Pass everything stored in the "prices" (sheet name) key back to the main.py file and
# store it in a variable called sheet_data, so that you can print the sheet_data from main.py
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)