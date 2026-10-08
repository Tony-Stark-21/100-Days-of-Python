import datetime
import requests_cache
from dotenv import load_dotenv

load_dotenv()
requests_cache.install_cache('flight_cache', backend='sqlite', expire_after=3600)

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

today = datetime.date.today()
six_months_from_now = today + datetime.timedelta(days=30)

sheet_data = data_manager.get_data()
sheet_rows = sheet_data["sheet1"]

print("Checking spreadsheet for missing location tokens...")
for row in sheet_rows:
    if not row["iataCode"] or row["iataCode"] == "":
        print(f"Discovering code for {row['city']}...")
        discovered_code = flight_search.get_iata_code(row["city"])
        if discovered_code and discovered_code != "N/A":
            data_manager.update_destination_codes(row_id=row["id"], new_iata_code=discovered_code)
            row["iataCode"] = discovered_code


print("\nScanning market arrays for flight deals...")

sheet_data = data_manager.get_data()
sheet_rows = sheet_data["sheet1"]

customer_data = data_manager.get_customer_emails()

for row in sheet_rows:
    destination_code = row["iataCode"]
    budget_threshold = row["lowestPrice"]

    if destination_code and destination_code != "N/A":
        print(f"Searching flights: PHC -> {destination_code} (Max Budget: USD {budget_threshold})...")

        raw_flight_payload = flight_search.check_prices(destination_code=destination_code)
        cheapest_deal = find_cheapest_flight(raw_flight_payload, return_date=six_months_from_now)
        if cheapest_deal and cheapest_deal.price < budget_threshold:
            print(f"🚨 DEAL FOUND! PHC to {row['city']} is only USD {cheapest_deal.price}!")

            alert_message = f"Low price alert! Only USD {cheapest_deal.price} to fly from {cheapest_deal.origin_airport} to {cheapest_deal.destination_airport}, departing on {cheapest_deal.out_date}."
            if cheapest_deal.stops > 0:
                alert_message += f"\n\n⚠️ Flight has {cheapest_deal.stops} stop(s), via {cheapest_deal.via_city}."
            for user in customer_data["users"]:
                if "whatIsYourEmail?" in user:
                    subscriber_email = user["whatIsYourEmail?"]
                    subscriber_name = user["whatIsYourFirstName?"]
                    print(f"Dispatched email confirmation row payload to: {subscriber_name} ({subscriber_email})")
                    notification_manager.send_emails(message_body=alert_message, destination_email=subscriber_email)
