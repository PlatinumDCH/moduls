from solid.o_open_close.simply_exemple.storage import Storage, JsonStorage, YamlStorage

class StorageService:
    def __init__(self, storage:Storage):
        self.storage = storage
    
    def get(self, key):
        return self.storage.get_value(key)



if __name__ == '__main__':

    storage_json = StorageService(JsonStorage('solid/o/simply_exemple/data.json'))
    storage_yaml = StorageService(YamlStorage("solid/o/simply_exemple/data.yaml"))
    print(storage_json.get("username"))
    print(storage_yaml.get("username"))