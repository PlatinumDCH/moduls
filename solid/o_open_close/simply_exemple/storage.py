import json
import yaml


class Storage:

    def get_value(self, key):
        raise NotImplementedError


class JsonStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, "r") as file:
            data = json.load(file)
            return data.get(key, None)


class YamlStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data.get(key, None)
