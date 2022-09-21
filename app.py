from flask import Flask, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route('/')
def SCORING():
    #load data
    with open('./Donnees_Dashboard.pkl', 'rb') as features_data:
        data = pickle.load(features_data)
    Donnees_API = data.to_dict()
    return jsonify(Donnees_API)

if __name__ == "__main__":
        app.run()