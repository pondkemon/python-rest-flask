from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    result = 0
    if request.method == "POST":
        input_value = request.form["input_value"]
        result=input_value * 2
    return jsonify(
        prediction=result
    ),201
