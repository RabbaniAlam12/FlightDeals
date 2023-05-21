import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/06df0a8e46bb6002a1809f757e041e5b/flightDeals/data'


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
