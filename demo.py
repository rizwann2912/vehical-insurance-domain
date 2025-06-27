from src.pipline.training_pipeline import TrainPipeline
from src.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact,DataIngestionArtifact
pipeline = TrainPipeline()
# pipeline.run_pipeline()

# # data_transformation_artifact = DataTransformationArtifact(transformed_object_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\24_06_2025_01_50_07\data_transformation\transformed_object\preprocessing.pkl',
# #                                                           transformed_train_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\24_06_2025_01_50_07\data_transformation\transformed\train.npy',
# #                                                           transformed_test_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\24_06_2025_01_50_07\data_transformation\transformed\test.npy')
# # pipeline.start_model_training(data_transformation_artifact=data_transformation_artifact)
data_ingestion_artifact = DataIngestionArtifact(
                                                train_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\27_06_2025_21_55_21\data_ingestion\ingested\train.csv',
                                                test_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\27_06_2025_21_55_21\data_ingestion\ingested\test.csv')

data_validation_artifact = pipeline.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
data_transformation_artifact = pipeline.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
                                    data_validation_artifact=data_validation_artifact)

model_trainer_artifact = pipeline.start_model_training(data_transformation_artifact=data_transformation_artifact)
model_evaluation_artifact = pipeline.start_model_evaluation(data_ingestion_artifact=data_ingestion_artifact,
                                                        model_trainer_artifact=model_trainer_artifact)
if not model_evaluation_artifact.is_model_accepted:

    exit(0)
model_pusher_artifact = pipeline.start_model_pusher(model_evaluation_artifact=model_evaluation_artifact)