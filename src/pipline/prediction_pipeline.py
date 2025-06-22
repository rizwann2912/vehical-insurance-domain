import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion


from src.entity.config_entity import DataIngestionConfig

from src.entity.artifact_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def start_data_ingestion(self):

        try:
            logging.info(f'Entered the start_data_ingestion emthod of TrainPipeline class')
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e,sys)
    def run_pipeline(self):

        try:
            data_ingestion_artifact = self.start_data_ingestion()
        
        except Exception as e:
            raise MyException(e,sys)

