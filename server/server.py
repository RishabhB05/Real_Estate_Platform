# flask is a module that helps in creating web applications in Python
from flask import Flask, jsonify, request 
app = Flask(__name__)  # Create a Flask application instance
import util

# Load artifacts once at startup so location data is ready
util.load_save_artifacts()

# bulding routes
@app.route('/get_location')
def get_location():
    # This route returns a JSON response with location data
    response = jsonify({
        'location': util.get_location()
    })

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    location = request.form['location']

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    
    return response




if __name__ == '__main__':
    print("Starting the server...")  # Print a message indicating the server is starting
    app.run()

