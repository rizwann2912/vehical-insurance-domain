import sys 
import numpy as np
import pandas as pd
from typing import Optional

from src.exception import MyException
from src.logger import logging
from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME



class Proj1Data:
    def __init__(self):
        try:
            self.mongodb_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e,sys)
        
    def export_collection_as_dataframe(self,collection_name, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongodb_client.database[collection_name]
            else:
                collection = self.mongodb_client[database_name][collection_name]

            print("Fetching data from MongoDB")
            df = pd.DataFrame(list(collection.find()))
            print(f'Data fecthed of length: {len(df)}')

            if "id" in df.columns.to_list():
                df.drop('id',axis =1)
            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise MyException(e,sys)