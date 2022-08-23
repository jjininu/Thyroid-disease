import os
import sys

from insurance.exception import CustomException
from insurance.util.util import load_object

import pandas as pd


class InsuranceData:

    def __init__(self,
                 age :  int,
                 sex_male : int,
                 bmi :   float,
                 children: int,
                 smoker_yes:  int,
                 region_northwest: int,
                 region_southeast : int,
                 region_southwest : int,
                 charges: float = None
                 ):    
                
        try:
            
            self.age = age
            self.sex_male = sex_male
            self.bmi = bmi
            self.children = children
            self.smoker_yes = smoker_yes
            self.region_northwest = region_northwest
            self.region_southeast = region_southeast
            self.region_southwest = region_southwest
            self.charges = charges

        except Exception as e:
            raise CustomException(e, sys) from e

    def get_insurance_input_data_frame(self):
        try:
            insurance_input_dict = self.get_insurance_data_as_dict()
            return pd.DataFrame(insurance_input_dict)
        except Exception as e:
            raise CustomException(e, sys) from e

    def get_insurance_data_as_dict(self):
        try:
            input_data = {
               "age" : [self.age],
                "sex_male" : [self.sex_male],
                "bmi" : [self.bmi],
                "children" : [self.children],
                "smoker_yes" : [self.smoker_yes],
                "region_northwest" : [self.region_northwest],
                "region_southeast" : [self.region_southeast],
                "region_southwest" : [self.region_southwest]}
            return input_data
        except Exception as e:
            raise CustomException(e, sys)


class InsurancePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise CustomException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise CustomException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            charges = model.predict(X)
            return charges
        except Exception as e:
            raise CustomException(e, sys) from e