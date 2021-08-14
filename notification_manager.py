# This class is responsible for sending notifications with the deal flight details.
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
# account_sid and auth_token from Twilio
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


class NotificationManager():
    # send an SMS with enough information to book the flight
    def __init__(self, departure_city, departure_iata_code, departure_date, arrival_date):
        self.city_name = departure_city
        self.city_iata_code = departure_iata_code
        self.departure_date = departure_date
        self.arrival_date = arrival_date

    def send_price_alert(self, price, city_name, city_iata_code):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert: ✈️ Only £{price} to fly from {self.city_name}-{self.city_iata_code}, to "
                 f"{city_name}-{city_iata_code}, from {self.departure_date} to {self.arrival_date}.",

            from_="+19494384494",
            to="+14088342564"
        )
