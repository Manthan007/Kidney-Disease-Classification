from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e

STAGE_NAME = "prepare base model stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e