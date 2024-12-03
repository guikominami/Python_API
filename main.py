import requests
import json

# e o tempo entre as lutas tbm pq isso afeta a recuperação dos danos e corte de peso


# Nested Dictionaries
# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


def filter_data(data_dict, key_description, filter_data_description) -> list:

    list_fighters = []

    for key_master, obj in data_fighters.items():

        for key_child in obj:

            try:
                if filter_data_description in obj[key_description]:

                    list_fighters.append(obj)
                    break
            except:
                print(f"Fighter {key_master} doesn´t have a place of birth")
                break

    return list_fighters


def filter_data_size(data_dict, key_description, filter_data_description) -> list:

    list_fighters = []

    for key_master, obj in data_fighters.items():

        for key_child in obj:

            try:
                if int(obj[key_description]) > filter_data_description:

                    list_fighters.append(obj)
                    break
            except:
                print("Erro")
                break

    return list_fighters


def filter_data_peformance(data_dict, filter_data_description) -> list:

    list_fighters = []

    for key_master, obj in data_fighters.items():

        for key_child in obj:

            try:
                if (int(obj["wins"]) - int(obj["losses"])) > filter_data_description:

                    list_fighters.append(obj)
                    break
            except:
                print("Erro")
                break

    return list_fighters


url = "https://api.octagon-api.com/rankings"
url = "https://api.octagon-api.com/fighters"

response = requests.get(url)
data_fighters = response.json()

# print("filtro de lutadores por país")
# data_fighters_filtered = filter_data(data_fighters, "placeOfBirth", "Brazil")
# data_fighters_sorted = sorted(
#     data_fighters_filtered, key=lambda d: int(d["wins"]), reverse=True
# )

# for fighters in data_fighters_sorted:
#     print(
#         f'name: {fighters["name"]} - wins: {fighters["wins"]} - losses: {fighters["losses"]}'
#     )

# print("filtro de lutadores com vitória > 30")
# data_fighters_filtered = filter_data_size(data_fighters, "wins", 30)
# data_fighters_sorted = sorted(
#     data_fighters_filtered, key=lambda d: int(d["wins"]), reverse=True
# )

# for fighters in data_fighters_sorted:
#     print(
#         f'name: {fighters["name"]} - wins: {fighters["wins"]} - losses: {fighters["losses"]}'
#     )

print("filtro de lutadores com vitória menos derrota > 25")
data_fighters_filtered = filter_data_peformance(data_fighters, 20)
data_fighters_sorted = sorted(
    data_fighters_filtered, key=lambda d: int(d["wins"]), reverse=True
)

for fighters in data_fighters_sorted:
    print(
        f'name: {fighters["name"]} - wins: {fighters["wins"]} - losses: {fighters["losses"]}'
    )
