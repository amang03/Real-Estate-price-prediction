from flask import Flask, request, jsonify
from server import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
from flask import send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
@app.route('/')
def home():
    return send_from_directory(os.path.join(BASE_DIR, 'client'), 'app.html')
print("Starting Python Flask Server For Home Price Prediction...")
util.load_saved_artifacts()
if __name__ == "__main__":
    app.run()