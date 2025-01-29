from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionPipeline
from src.datascience.config.config import ConfigurationManager
from src.datascience.pipeline.data_validation import DataValidator
from src.datascience.entity.config_entity import DataTransformationConfig
from src.datascience.pipeline.data_transformation import DataTransformation
from src.datascience.pipeline.data_training import Trainer
from src.datascience.pipeline.data_evaluation import EvaluateModel

logger.info("Welcome tomy logging standards")

STAGE_NAME="Data Ingestion Stage"
if __name__ =="__main__":
    try:
        logger.info(f"Stage name {STAGE_NAME} started")
        obj =DataIngestionPipeline()
        obj.initialize_data_ingestion()
        logger.info(f"Stage name {STAGE_NAME} ended")
        logger.info("Data Validation has been started")
        obj=ConfigurationManager()
        data_validation_config=obj.get_data_validation_config()
        data_validator=DataValidator(config=data_validation_config)
        output=data_validator.validate_all_columns()
        logger.info("Data Validation has ended")
    except Exception as e:
        logger.error(e)
        raise e
try:
    logger.info(f"Data Transformation has started")
    obj=ConfigurationManager()
    config=obj.get_data_transformation_config()
    DataTransformation(config).splitting_data()
    logger.info(f"Data Transformation ended ,data saved to artifacts.")
except Exception as e:
    raise e    


try:
    logger.info(f"Data Training has started")
    obj= ConfigurationManager()
    config=obj.get_data_training_config()
    Trainer(config).train_model()
    logger.info(f"Data Training has ended")
except Exception as e:
    print(e)

try:
    obj= ConfigurationManager()
    config=obj.get_evaluation_config_data()
    EvaluateModel(config).log_data_to_mlflow()
    

except Exception as e:
    print(e)