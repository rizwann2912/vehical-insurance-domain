import sys
import numpy as np
import pandas as pd
from imblearn.combine import SMOTEENN
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.compose import ColumnTransformer

from src.constants import TARGET_COLUMN, SCHEMA_FILE_PATH, CURRENT_YEAR
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import save_object,save_numpy_array_data, read_yaml_file

class DataTransformation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):
        
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e,sys)
        
    def get_data_transformer_object(self) -> Pipeline:
        logging.info("Entered get_data_transformer_object method of DataTransformation class")
        try:
            numeric_transformer = StandardScaler()
            min_max_scaler = MinMaxScaler()
            logging.info("Transformers Initialized: StandardScaler - MinMaxScaler")

            #Load Schema configurations
            num_features = self._schema_config['num_features']
            mm_columns = self._schema_config['mm_columns']
            logging.info('Colunns added drom schema')

            #Creating Preprocessor Pipeline
            preprocessor = ColumnTransformer(
                transformers=[
                    ("StandardScaler",numeric_transformer,num_features),
                    ("MinMaxScaler", min_max_scaler,mm_columns)
                ],
                remainder='passthrough'
            )
            # erapping everything in single pipeline
            final_pipeline = Pipeline(steps=[("Preprocessor",preprocessor)])
            logging.info("Final Pipeline Ready!!")
            logging.info("Exited get_data_transformer_object method of DataTransformation class")
            return final_pipeline
        except Exception as e:
            raise MyException(e,sys)
    
    def categorical_transformation(self,df):
        try:
            logging.info("Mapping 'Gender' column to binary values")
            df['Gender'] = df['Gender'].map({'Male':1,'Female':0}).astype(int)

            logging.info("Dropping 'id' column")
            drop_col = self._schema_config['drop_columns']
            if drop_col in df.columns:
                df = df.drop(drop_col, axis=1)
            
            logging.info('Creating dummy variable for categorical features')
            print(df.nunique().sort_values(ascending=False).head(10))

            df = pd.get_dummies(df,drop_first=True)

            logging.info('Renaming speciifc columns')
            df = df.rename(columns={
            "Vehicle_Age_< 1 Year": "Vehicle_Age_lt_1_Year",
            "Vehicle_Age_> 2 Years": "Vehicle_Age_gt_2_Years"               
            })
            for col in ["Vehicle_Age_lt_1_Year", "Vehicle_Age_gt_2_Years", "Vehicle_Damage_Yes"]:
                if col in df.columns:
                    df[col] = df[col].astype('int')
            


            return df
        except Exception as e:
            raise MyException(e,sys)
        

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info('Data Transformation started')
            if not self.data_validation_artifact.validation_status:
                raise Exception(self.data_validation_artifact.message)
            
            train_df = pd.read_csv(filepath_or_buffer=self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(filepath_or_buffer=self.data_ingestion_artifact.test_file_path)

            logging.info('Training and testing data loaded')

            input_features_train_df = train_df.drop(TARGET_COLUMN,axis = 1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            input_features_test_df = test_df.drop(TARGET_COLUMN,axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            logging.info("Input and Target cols defined for both train and test df.")

            input_features_train_df = self.categorical_transformation(input_features_train_df)
            input_features_test_df = self.categorical_transformation(input_features_test_df)
            logging.info("Custom transformations applied to train and test data")

            logging.info('Starting data transformation')
            preprocessor = self.get_data_transformer_object()
            logging.info('Got the preprocessor object')

            logging.info('Initializing transformation for training-data')
            input_features_train_arr = preprocessor.fit_transform(input_features_train_df)
            logging.info('Initializing transformation for testing-data')
            input_features_test_arr =preprocessor.fit_transform(input_features_test_df)
            logging.info("Transformation done end to end to train-test df.")

            logging.info('Applying SMOTEEN for handling Imbalanced dataset')
            smt = SMOTEENN(sampling_strategy='minority')
            input_feature_train_final,target_feature_train_final =smt.fit_resample(input_features_train_arr,target_feature_train_df)
            input_feature_test_final,target_feature_test_final = smt.fit_resample(input_features_test_arr,target_feature_test_df)
            logging.info("SMOTEENN applied to train-test df.")

            train_arr = np.c_[input_feature_train_final,np.array(target_feature_train_final)]
            test_arr = np.c_[input_feature_test_final,np.array(target_feature_test_final)]
            logging.info("feature-target concatenation done for train-test df.")
            
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,test_arr)
            logging.info("Saving transformation object and transformed files.")

            logging.info('Data Transformation completed Succesfuuly')
            return DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_train_file_path = self.data_transformation_config.transformed_test_file_path
            )
        except Exception as e:
            raise MyException(e,sys)
        