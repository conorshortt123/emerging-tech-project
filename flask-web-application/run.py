# flask for web app.
import flask as fl
from flask import request
# numpy for numerical work.
import numpy as np
# To import decision_tree_model
import pickle

# Create a new web app.
app = fl.Flask(__name__)


# Add root route.
@app.route("/")
def home():
    return fl.render_template('index.html')


# Add power predictor route.
@app.route('/api/get-power-prediction')
def power_prediction():
    # Gets request arguments
    args = request.args

    # Creates a key : value pair containing the power prediction as a string with "kW/s" formatted on to it.
    val = {"value": str(predict_power(args.get('windspeed'))) + " kW/s"}

    # Returns key : value pair.
    return val


def predict_power(wind_speed):
    # Load model from disk with pickle.
    filename = 'decision_tree_model/finalized_model.sav'
    model = pickle.load(open(filename, 'rb'))

    # Make prediction with model and return as a scalar value rather than an array.
    pred = model.predict([[wind_speed]])

    return np.asscalar(pred)
