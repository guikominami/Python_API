import requests
import json
from api import API

# e o tempo entre as lutas tbm pq isso afeta a recuperação dos danos e corte de peso


# Nested Dictionaries
# create a formatted string of the Python JSON object


url = "https://api.octagon-api.com/rankings"
url = "https://api.octagon-api.com/fighters"

api_fighters = API(url)
data_fighters = api_fighters.connect()

if data_fighters is not None:

    print("filtro de lutadores por país")

    data_fighters_filtered = api_fighters.filter_data(
        data_fighters, "placeOfBirth", "Brazil"
    )

    for fighters in data_fighters_filtered:
        print(
            f'name: {fighters["name"]} - wins: {fighters["wins"]} - losses: {fighters["losses"]}'
        )

    print("filtro de lutadores com vitória > 30")
    data_fighters_filtered = api_fighters.filter_data_size(data_fighters, "wins", 30)
    data_fighters_sorted = sorted(
        data_fighters_filtered, key=lambda d: int(d["wins"]), reverse=True
    )

    for fighters in data_fighters_sorted:
        print(
            f'name: {fighters["name"]} - wins: {fighters["wins"]} - losses: {fighters["losses"]}'
        )

    print("filtro de lutadores com vitória menos derrota > 25")
    data_fighters_filtered = api_fighters.filter_data_peformance(data_fighters, 20)
    data_fighters_sorted = sorted(
        data_fighters_filtered, key=lambda d: int(d["wins"]), reverse=True
    )

    for fighters in data_fighters_sorted:
        print(
            f'name: {fighters["name"]} - wins: {fighters["wins"]} - losses: {fighters["losses"]}'
        )
