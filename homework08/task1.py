class KeyValueStorage:
    def __init__(self, file_path):
        self.from_file = {}
        with open(file_path, "r") as file_storage:
            lines = file_storage.read().split("\n")
            for line in lines:
                if "=" not in line:
                    continue
                key, value = KeyValueStorage.validate_line(*line.split("="))
                self.from_file[key] = value
                line = file_storage.readline()

    def __getitem__(self, key):
        return self.from_file[key]

    def __getattr__(self, attr):
        return self.from_file[attr]

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


if __name__ == "__main__":
    storage = KeyValueStorage("/mnt/c/EPAM/homework-repository/homework08/task1.txt")
    a = storage["name"]  # will be string 'kek'
    b = storage.last_name  # will be 'top'
    c = storage.power  # will be integer 9001
