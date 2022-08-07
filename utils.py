import pickle
import json
import re
import numpy as np
import config

class SalaryPrediction():
    def __init__(self, Gender,Age, PhD):
      self.Gender = Gender 
      self.Age    = Age
      self.PhD    = PhD


    def load_model(self):
        with open (config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open (config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)



    def get_predicted_salary(self):
        self.load_model()   

        test_array=np.zeros(len(self.json_data['column']))
        test_array[0] = self.json_data['Gender'][self.Gender]
        test_array[1] = self.Age
        test_array[2] = self.json_data['PhD'][self.PhD]
        
        pred_salary = self.model.predict([test_array])
        return pred_salary

if __name__ == "__main__":
     Gender ='male'
     Age = 30
     PhD = 'yes'
     
     salary_pred = SalaryPrediction(Gender,Age, PhD)
     salary_pred.get_predicted_salary()