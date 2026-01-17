# flask is a module that helps in creating web applications in Python
from flask import Flask, jsonify, request 
app = Flask(__name__)  # Create a Flask application instance



@app.route('/home')
def home():
    return "Welcome to the Home Page!"  # Return a welcome message for the home page




if __name__ == '__main__':
    print("Starting the server...")  # Print a message indicating the server is starting
    app.run()
