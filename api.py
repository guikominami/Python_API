import json
import requests


class API:
    def __init__(self, url) -> None:
        self.url = url

    def connect(self):

        response = requests.get(self.url)

        if response.status_code != 404:
            try:
                data_fighters = response.json()
                return data_fighters

            except ValueError as e:
                raise e
        else:
            print("URL does not exist")

    def jprint(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        return text

    def filter_data(
        self,
        data_dict: dict,
        key_description,
        filter_data_description,
        sort_crescent=True,
    ) -> list:

        list_fighters = []

        for obj in data_dict.values():

            for key_child in obj:

                try:
                    if filter_data_description in obj[key_description]:

                        list_fighters.append(obj)
                        break
                except:
                    print(f"Fighter {obj['name']} doesn´t have a place of birth")
                    break

        if sort_crescent:
            data_fighters_sorted = sorted(
                list_fighters, key=lambda d: int(d["wins"]), reverse=True
            )

        return list_fighters

    def filter_data_size(
        self, data_dict: dict, key_description, filter_data_description
    ) -> list:

        list_fighters = []

        for obj in data_dict.values():
            for key_child in obj:

                try:
                    if int(obj[key_description]) > filter_data_description:

                        list_fighters.append(obj)
                        break
                except:
                    print("Erro")
                    break

        return list_fighters

    def filter_data_peformance(self, data_dict: dict, filter_data_description) -> list:

        list_fighters = []

        for key_master, obj in data_dict.items():

            # nesse dicionário, a chave é o nome do lutador
            # print(key_master)

            for key_child in obj:

                try:
                    if (
                        int(obj["wins"]) - int(obj["losses"])
                    ) > filter_data_description:

                        list_fighters.append(obj)
                        break
                except:
                    print("Erro")
                    break

        return list_fighters
