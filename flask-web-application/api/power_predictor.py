from __future__ import print_function
import numpy as np
from sklearn import tree
import os
import sys

def predict_power(wind_speed):

    filename="./api/powerproduction.csv"

    data = np.loadtxt(filename, delimiter=",", skiprows=1)

    # Split numpy array into two arrays, a two dimensional array for x-values, and one dimensional for y-values.
    x = data[:,[0]]
    y = (data[:,[1]]).reshape(-1)

    model = tree.DecisionTreeRegressor(max_depth=13).fit(x, y)

    pred = model.predict([[wind_speed]])

    return np.asscalar(pred)