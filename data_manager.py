import requests
from pprint import pprint
from endpoints import sheety_prices_endpoint

# The endpoints have been imported from another file
SHEETY_PRICES_ENDPOINT = sheety_prices_endpoint 


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url = SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["data"]
        pprint(data)

        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "datum": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
