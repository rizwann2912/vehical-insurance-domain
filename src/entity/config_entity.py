import os
from src.constants import *
from dataclasses import dataclass
from  datetime import datetime

TIMESTAMP = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name = PIPELINE_NAME
    artifact_dir = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp = TIMESTAMP

training_pipeline_config = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTION_DIR_NAME)
    feature_store_file_path = os.path.join(data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR,FILE_NAME)
    training_file_path = os.path.join(data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TRAIN_FILE_NAME)
    testing_file_path = os.path.join(data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TEST_FILE_NAME)
    train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name = DATA_INGESTION_COLLECTION_NAME

@dataclass
class DataValidationConfig:
    data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,DATA_VALIDATION_DIR_NAME)
    data_validation_file_report_path = os.path.join(data_validation_dir,DATA_VALIDATION_REPORT_FILE_NAME)

@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRAIN_FILE_NAME.replace("csv", "npy"))
    transformed_test_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                   TEST_FILE_NAME.replace("csv", "npy"))
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     PREPROCSSING_OBJECT_FILE_NAME)
    
@dataclass
class ModelTrainerConfig:
    model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir,MODEL_TRAINER_DIR_NAME)
    trained_model_file_path =os.path.join(model_trainer_dir,MODEL_TRAINER_TRAINED_MODEL_DIR,MODEL_TRAINER_TRAINED_MODEL_NAME)
    expected_accuracy =MODEL_TRAINER_EXPECTED_SCORE
    model_config_file_path = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
    _n_estimators = MODEL_TRAINER_N_ESTIMATORS
    _min_samples_split = MODEL_TRAINER_MIN_SAMPLES_SPLIT
    _min_samples_leaf = MODEL_TRAINER_MIN_SAMPLES_LEAF
    _max_depth = MIN_SAMPLES_SPLIT_MAX_DEPTH
    _criterion = MIN_SAMPLES_SPLIT_CRITERION
    _random_state = MIN_SAMPLES_SPLIT_RANDOM_STATE

@dataclass
class ModelEvaluationConfig:
    changed_threshold_score = MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
    bucket_name = MODEL_BUCKET_NAME
    s3_model_key_path = MODEL_FILE_NAME

@dataclass
class ModelPusherCOnfig:
    bucket_name = MODEL_BUCKET_NAME
    s3_model_key_path = MODEL_FILE_NAME
    
@dataclass
class VehiclePredictorConfig:
    model_file_path:str = MODEL_FILE_NAME
    model_bucket_name :str = MODEL_BUCKET_NAME