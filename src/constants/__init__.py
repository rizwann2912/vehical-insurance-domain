import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()
# For MongoDB connection
DATABASE_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"
MONGODB_URL_KEY = os.getenv("MONGODB_URL")

PIPELINE_NAME = ""
ARTIFACT_DIR = "artifact"

TARGET_COLUMN = 'Response'
CURRENT_YEAR = 2025

PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl" 

MODEL_FILE_NAME = "model.pkl"

FILE_NAME = 'data.csv'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'
SCHEMA_FILE_PATH = os.path.join('config','schema.yaml')


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "Proj1-Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

"""
Data Validation related constant 
"""
DATA_VALIDATION_DIR_NAME = 'data_validation'
DATA_VALIDATION_REPORT_FILE_NAME = 'report.yaml'

"""
Data Transformation related constant
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"