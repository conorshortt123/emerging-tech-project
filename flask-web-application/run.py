# flask for web app.
import flask as fl
from flask import request
# numpy for numerical work.
import numpy as np
# to navigate to api directory and retrieve power_predictor.py
import sys
sys.path.insert(1, './api')
from power_predictor import predict_power

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return fl.render_template('index.html')

# Add power predictor route.
@app.route('/api/get-power-prediction')
def power_prediction():

  args = request.args

  val = {"value": str(predict_power(args.get('windspeed'))) + " kW/s"}
  
  return val
