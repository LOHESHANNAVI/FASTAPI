from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["test_db"]
collection = db["test_collection"]

def get_mongo_data():
    data = list(collection.find({}, {"_id": 0}))
    return data