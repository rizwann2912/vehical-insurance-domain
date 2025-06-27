from src.pipline.training_pipeline import TrainPipeline
from src.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
pipeline = TrainPipeline()
pipeline.run_pipeline()

# data_transformation_artifact = DataTransformationArtifact(transformed_object_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\24_06_2025_01_50_07\data_transformation\transformed_object\preprocessing.pkl',
#                                                           transformed_train_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\24_06_2025_01_50_07\data_transformation\transformed\train.npy',
#                                                           transformed_test_file_path=r'C:\Users\mdriz\Youtube tut\mlops\vehical-insurance-domain\artifact\24_06_2025_01_50_07\data_transformation\transformed\test.npy')
# pipeline.start_model_training(data_transformation_artifact=data_transformation_artifact)

model_trainer_artifact = ModelTrainerArtifact()