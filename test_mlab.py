from pymongo import MongoClient
import os

def get_fcm_token(device_id):
    client = MongoClient(os.environ['AWS_MONGO_KEY'])
    db = client['iot-retail']
    collection = db['fcm_mapping']
    fcm_token = "none"
    cursor = collection.find({"device_id": device_id})
    if cursor.count()>0:
        fcm_token = cursor[0]['fcm_token']
    return fcm_token
