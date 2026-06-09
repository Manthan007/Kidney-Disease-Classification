import mlflow
import dagshub

# Initialize DagsHub integration
dagshub.init(repo_owner="Manthan007", repo_name="Kidney-Disease-Classification", mlflow=True)

from cnnClassifier.components.training import Training
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger

STAGE_NAME = "Training stage"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Start an MLflow run
        with mlflow.start_run():
            config = ConfigurationManager()
            training_config = config.get_training_config()
            mlflow.set_tag("stage", "training")
            
            # Log hyperparameters from your config
            mlflow.log_params(training_config.all_params)

            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            
            # Train the model and log training metrics
            history = training.train() # Ensure your .train() method returns the history object
            
            # Log final accuracy/loss
            mlflow.log_metric("accuracy", history.history['accuracy'][-1])
            mlflow.log_metric("loss", history.history['loss'][-1])
            
            # Log the final trained model
            mlflow.keras.log_model(training.model, "model")

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        raise e