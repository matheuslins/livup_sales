from pymongo import MongoClient

from src.settings import DB_HOST


class DBHandler:

    def __init__(self):
        self.db = None
        self.collection = None

    def connect(self):
        client = MongoClient(DB_HOST)
        self.db = client.get_database('livup_sales')
        self.collection = self.db['sales']

    def save_items(self, items):
        self.collection.insert_many(items)
