import json

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            # print(f"在JSON类中读取的结果: {self.file_path}: {json_data}")
            return json_data

    def get_test_data(self, test_method_name):
        test_data = self.read_json()
        return test_data.get(test_method_name, {})
