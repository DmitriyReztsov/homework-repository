class KeyValueStorage:
    def __init__(self, file_path):
        with open(file_path, "r") as file_storage:
            lines = file_storage.read().split("\n")
            for line in lines:
                if "=" not in line:
                    continue
                key, value = KeyValueStorage.validate_line(*line.split("="))
                self.__dict__[key] = value
                line = file_storage.readline()

    def __getitem__(self, key):
        return self.__dict__[key]

    @staticmethod
    def validate_line(key, value):
        try:
            key = int(key)
        except ValueError:
            pass
        if not isinstance(key, str):
            raise ValueError("key should be string")
        try:
            value = int(value)
        except ValueError:
            pass
        return key, value
