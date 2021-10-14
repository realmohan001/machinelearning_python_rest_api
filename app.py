from flask import Flask,request
import json
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

model = joblib.load('flight-provision.joblib')


@app.route("/predict",methods=['POST'])
def predict():
    event = json.loads(request.data)
    print(event['value'])	
    predicted=model.predict([ [ event['value'] ] ])
    print(predicted)
    ts=np.array_str(predicted)
    return {"json": ts};
