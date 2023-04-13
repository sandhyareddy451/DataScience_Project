import os
import sys
import pandas as pd
from dataclass import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')


class DataIngestion:
    def__init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion:
        logging.info("Enter the data Ingestion method or components")
        try:
         
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the data set as dataframe")
            os.makedirs(os.path.join(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("split into train and test data")
            train_set,test_set=train_test_split(df,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("ingestion of data is completed")

            return(

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)

    if __name__=='__main__':
        obj=DataIngestionConfig()
        obj.initiate_data_ingestion()