import pandas as pd
import os
from src.datascience.utils.common import save_model
from src.datascience import logger
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from src.datascience.config.config import DataTraningConfig
import joblib 

class Trainer:
    def __init__(self,config=DataTraningConfig):
        self.config=config

    def train_model(self):
        train_data= pd.read_csv(self.config.train_data_path)
        test_data= pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column],axis=1)
        test_x = test_data.drop([self.config.target_column],axis=1)
        train_y= train_data[self.config.target_column]
        test_y= test_data[self.config.target_column]
        lr = ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=42)
        lr.fit(train_x,train_y)
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))
        

