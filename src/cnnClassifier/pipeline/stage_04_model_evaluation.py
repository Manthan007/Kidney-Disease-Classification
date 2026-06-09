import mlflow
import dagshub

from cnnClassifier.utils.common import copy_model_to_folder

# Initialize DagsHub integration
dagshub.init(repo_owner="Manthan007", repo_name="Kidney-Disease-Classification", mlflow=True)

from cnnClassifier.components.model_evaluation import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger

STAGE_NAME = "Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        copy_model_to_folder(
            source_path="artifacts/training/model.keras", 
            target_folder="model"
        )
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        raise e