
from flask import Flask, render_template, render_template_string,jsonify,request
import config
from data_set.utils import SalaryPrediction

app = Flask(__name__)

@app.route('/')


def hello_flask():

    print("Welcome to Data science")
    return 'vasanti'

@app.route('/Salary_Predict')

def get_predicted_charges():
     Gender ='male'
     Age = 30
     PhD = 'yes'

     salary_pred = SalaryPrediction(Gender,Age, PhD)
     salary = salary_pred.get_predicted_salary()

     return jsonify({"Result": f"Predicted charges is :{salary}"})

if __name__ == "__main__":
 app.run()


