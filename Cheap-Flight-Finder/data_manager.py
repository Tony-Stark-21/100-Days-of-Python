import requests
import os



class DataManager:
    def get_data(self):
        self.sheety_url = "https://api.sheety.co/e7084c9eef590c03d918f1d7288c38a4/flightTracker/sheet1"
        self.sheety_username = os.environ.get("SHEETY_USERNAME")
        self.sheety_password = os.environ.get("SHEETY_PASSWORD")

        self.sheety_response = requests.get(self.sheety_url, auth=(self.sheety_username, self.sheety_password))
        self.data = self.sheety_response.json()
        return self.data
        # pprint(f"User: {self.sheety_username}, Pass: {self.sheety_password}")

    def update_destination_codes(self, row_id, new_iata_code):
        update_url = f"{self.sheety_url}/{row_id}"
        new_data = {
            "sheet1": {
                "iataCode": new_iata_code
            }
        }
        response = requests.put(update_url, json=new_data, auth=(os.environ.get("SHEETY_USERNAME"), os.environ.get("SHEETY_PASSWORD")), headers={"Content-Type": "application/json"})
        # print(response.text)


