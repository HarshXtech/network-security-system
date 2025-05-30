import os
import sys
import json
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import pymongo
# to validate the https connections / to verify weather they are secured / will ensure trusted certificate autherity 
import certifi
import pymongo.mongo_client
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

# will give the path of security certificate like - (HTTPS / TLS)
ca = certifi.where()

# ETL pipeline
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def cv_to_json_converter(self, filepath):
        try:
            data = pd.read_csv(filepath)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values()) 
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return f'{len(self.records)} Data Inserted'
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = "network_data\phisingData.csv"
    DATABASE = "HarshAI"
    COLLECTION = "network_data"
    networkObj = NetworkDataExtract()
    records = networkObj.cv_to_json_converter(FILE_PATH)
    print(records)
    no_of_records = networkObj.insert_data_to_mongodb(records, DATABASE, COLLECTION)

    print(no_of_records)