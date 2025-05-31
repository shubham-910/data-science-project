from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingetion import DataIngestion
#   from src.mlproject.components.data_ingetion import DataIngetionConfig

if __name__ == "__main__":
    logging.info("The execution has started.")

    try:
        #data_ingetion_config=DataIngetionConfig()
        data_ingetion = DataIngestion()
        data_ingetion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)