from pymongo import MongoClient
from config.settings import Settings

class MongoConnection:
    client = MongoClient( Settings.MONGO_URI)

    database = client[Settings.DATABASE_NAME]

    @staticmethod
    def get_database():
        return MongoConnection.database