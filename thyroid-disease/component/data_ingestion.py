from threading import local
from thyroid-disease.entity.config_entity import DataIngestionConfig
import sys,os
from thyroid-disease.exception import CustomException
from thyroid-disease.logger import logging
from thyroid-disease.entity.artifact_entity import DataIngestionArtifact
import tarfile
import numpy as np
import urllib.request

import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from thyroid-disease.util.util import read_write_file
import shutil


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise Exception(e)
    

   

    def transfer_data(self):
        
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            os.makedirs(raw_data_dir,exist_ok=True)
            local_file = self.data_ingestion_config.local_file
            
            shutil.copy(local_file, raw_data_dir)
            return local_file
        except Exception as e:
            raise Exception(e)
    
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            thyroid-disease_file_path = os.path.join(raw_data_dir,file_name)


            logging.info(f"Reading csv file: [{thyroid-disease_file_path}]")
            thyroid-disease_data_frame = pd.read_csv(thyroid-disease_file_path)
            #thyroid-disease_data_frame  =pd.get_dummies(thyroid-disease_data_frame,drop_first=True)


            
            

            logging.info(f"Splitting data into train and test")
            train_set = None
            test_set = None

            train, test = train_test_split(thyroid-disease_data_frame, test_size = 0.2, stratify=df[['binaryClass']],shuffle=True)


            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            "train"+".csv")

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        "test"+".csv")
            os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
            os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
            train.to_csv(train_file_path,index=False)
            test.to_csv(test_file_path,index=False)
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise Exception(e) 

    def initiate_data_ingestion_from_local(self):
        try:
            self.transfer_data()
            return self.split_data_as_train_test()

        except Exception as e:
            raise Exception(e)
    
    


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")
