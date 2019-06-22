import json
import os

from src.database import DBHandler


class AppHandler:

    def __init__(self):
        self.sales = []

    def run(self):
        items = self.read_local_file('files/sales.json')
        self.save_in_data_base(items)

    @staticmethod
    def read_local_file(file_path):
        full_path = f"{os.path.dirname(os.path.abspath(__file__))}/{file_path}"
        file_exists = os.path.isfile(full_path)
        if not file_exists:
            return []
        with open(full_path) as file:
            items = json.loads(file.read())
            return [item for item in items]

    @staticmethod
    def save_in_data_base(items):
        db = DBHandler()
        db.connect()
        db.save_items(items)
