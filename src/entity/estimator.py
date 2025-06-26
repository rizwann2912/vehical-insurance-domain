import sys

from pandas import DataFrame
import pandas as pd
from sklearn.pipeline import Pipeline

from src.logger import logging
from src.exception import MyException

class TargetValueMapping:
    def __init__(self):
        self.yes = 0
        self.no = 1

    def _asdict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))
    

class MyModel:
    def __init__(self,preprocessing_objecet:Pipeline,
                 trained_model_object:object):
        self.preprocessing_object = preprocessing_objecet
        self.trained_model_obejct = trained_model_object

    def predict(self,dataframe:DataFrame) -> DataFrame:
        try:
            logging.info('Starting prediction process')

            transformed_feature = self.preprocessing_object.transform(dataframe)

            logging.info('using the trained model to get the predictions')
            predictions = self.trained_model_obejct.predict(transformed_feature)

            return predictions
        except Exception as e:
            raise MyException(e,sys) from e
        
    def __repr__(self):
        return f"{type(self.trained_model_obejct).__name__}()"
    def __str__(self):
        return f"{type(self.trained_model_obejct).__name__}()"