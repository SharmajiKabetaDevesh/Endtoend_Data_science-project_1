from src.datascience.config.config import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from src.datascience import logger
from pathlib import Path
class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def splitting_data(self):
        with open(Path('artifacts/data_validation/status.txt'),'r') as f:
            status=f.read().split(":")[-1]
    
            if(status=="True"):
               data=pd.read_csv(self.config.data_path)
               train,test=train_test_split(data)
               train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
               test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
               logger.info("Splitted the data into train and test")
               logger.info(f"Train Size:{train.shape}")
               logger.info(f"Test Size:{test.shape}")
            else:
                raise Exception("The data is not valid")

      