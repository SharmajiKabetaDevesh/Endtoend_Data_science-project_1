import os
import yaml
from src.datascience import logger
import json 
import joblib
from ensure import ensure_annotations
from box import box
from pathlib import Path
from typing import Any
from box import ConfigBox
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loading successfull")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Cretaed directory at:{path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,'w')as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    with open as f:
        context=json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(context)

@ensure_annotations
def save_model(data:Any,path:Path)->Any:
    joblib.dump(value=data,filename=path)
    logger.info(f"model saved to :{path}")

@ensure_annotations
def load_model(path:Path)->Any:
    model=joblib.load(path)
    logger.info(f"binary file loaded from:{path}")
    return model
