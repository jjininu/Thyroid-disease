from thyroid-disease.pipeline.pipeline import Pipeline
from thyroid-disease.exception import CustomException
from thyroid-disease.logger import logging
from thyroid-disease.config.configuration import Configuartion
from thyroid-disease.component.data_transformation import DataTransformation
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

