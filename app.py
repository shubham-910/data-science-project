from mlproject.components.data_transformation import DataTransformation
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingetion import DataIngestion
#   from src.mlproject.components.data_ingetion import DataIngetionConfig

if __name__ == "__main__":
    logging.info("The execution has started.")

    try:
        #data_ingetion_config=DataIngetionConfig()
        # data_ingetion = DataIngestion()
        # data_ingetion.initiate_data_ingestion()

        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        # model_trainer=ModelTrainer()
        # print(model_trainer.initiate_model_trainer(train_arr,test_arr))


    except Exception as e:
        raise CustomException(e,sys)