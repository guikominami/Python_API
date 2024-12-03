import requests
import json

# Nested Dictionaries


# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


url = "https://api.octagon-api.com/rankings"
url = "https://api.octagon-api.com/fighters"

response = requests.get(url)
dict_fighters = response.json()

# data = json.loads(data_json)

# print(type(dict_json))
# print(data_json.values())
# print(data_json.items())
# print(data_json.keys())

# fighters_data = dict_fighters.values()

# for fighter in fighters_data:
#     print(fighter)
# print(fighter['name'])
# print(fighter['category'])
# print(fighter['placeOfBirth'])

# for fighter in dict_fighters.values():
#     print(fighter)

# filter_result = {key : val for key, val in dict_fighters.items() if key.startswith('age')}
# print(filter_result)

print(jprint(dict_fighters))

# for fighter in dict_fighters.values():
#     if int(fighter['wins']) > 30:
#         print("name: ", fighter['name'])
#         print("wins: ", fighter['wins'])
#         print("country: ", fighter['placeOfBirth'])


# filter_result = {key : val for key, val in dict_fighters.values() if key.startswith('age')}

# filtered_list = list(filter(lambda d: "6" in d, dict_fighters))

# print(filtered_list)
