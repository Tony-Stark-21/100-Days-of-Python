import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv



class FlightSearch:

    def get_iata_code(self, city_name):
        self.serp_url = "https://serpapi.com/search"
        search = {
            "engine": "google_flights_autocomplete",
            "q":city_name,
            "api_key": os.environ.get("SERP_API_KEY"),
        }
        self.serp_requests = requests.get(self.serp_url, params=search)
        price_data = self.serp_requests.json()
        print(price_data)
        try:
            iata_code = price_data["suggestions"][0]["airports"][0]["id"]
            return iata_code
        except (KeyError, IndexError):
            return "N/A"

    def check_prices(self, destination_code):
        self.serp_url = "https://serpapi.com/search"
        today = datetime.today()
        six_months_from_now = today + timedelta(days=180)
        to_time = six_months_from_now.strftime('%Y-%m-%d')
        search1 = {
            "engine": "google_flights",
            "departure_id": "PHC",
            "arrival_id": destination_code,
            "currency": "NGN",
            "type": "2",
            "outbound_date": to_time,
            "api_key": os.getenv("SERP_API_KEY")
        }


        self.serp_response = requests.get(self.serp_url, params=search1)
        price_data = self.serp_response.json()
        return price_data
        # lowest_price = price_data["price_insights"]["lowest_price"]
        #
        # return lowest_price

    def cheapest_flight_object(self, destination_code) :
        self.serp_url = "https://serpapi.com/search"
        today = datetime.today()
        six_months_from_now = today + timedelta(days=180)
        to_time = six_months_from_now.strftime('%Y-%m-%d')
        search1 = {
            "engine": "google_flights",
            "departure_id": "PHC",
            "arrival_id": destination_code,
            "currency": "NGN",
            "type": "2",
            "outbound_date": to_time,
            "api_key": os.getenv("SERP_API_KEY")
        }

        self.serp_response = requests.get(self.serp_url, params=search1)
        return self.serp_response.json()
