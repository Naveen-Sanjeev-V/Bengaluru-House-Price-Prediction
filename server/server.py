# import flast module
from flask import Flask,jsonify,request
import util
from flask_cors import CORS

# instance of flask application
app = Flask(__name__)
CORS(app)

# home route that returns below text when root url is accessed
@app.route('/get_location_names')
def get_location_name():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price", methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    return response

if __name__ == '__main__': 
    util.load_saved_artifacts()
    app.run()