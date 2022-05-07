import json
from data.interfaces.item_interface import DataInterface
from data.interfaces.json.json_item import JsonItem

JSON_DEFAULT = ("data/Vulnerability_data.json")


class JsonReader(DataInterface):
    json_file = JSON_DEFAULT
    items = None

    def change_json_file(self, json_file):
        self.json_file = json_file

    """
    Get items from json

    :param json_file: the file to read the json data from
    :returns: the items that have been parsed from the file
    """
    def get_items_from_file(self, json_file):
        if self.items:
            return self.items

        file = None
        items = []

        try:
            # Opening JSON file
            file = open(json_file)
            json_data = json.load(file)

            # Iterating through the json
            # list
            for line in json_data:
                print(line)

            for data in json_data['items']:
                item = JsonItem(data)
                items.append(item)
        except FileNotFoundError:
            print("File not found")
        finally:
            # Closing file
            if file:
                file.close()

        return items

    """
    Get items from default json

    :returns: the items that have been parsed from the file
    """
    def get_items(self):
        return self.get_items_from_file(self.json_file)