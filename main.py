# Author: Hasan Siddiqui
# Version: 1.0
# Date: Mar 22, 2024

from flask import Flask, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Enable CORS
CORS(app)

# Database connection
app.config['MONGODB_SETTINGS'] = {
    'host': os.getenv('MONGODB_URI')
}
db = MongoEngine(app)

# Import routers
from routes.book_routes import book_routes
from routes.user_routes import user_routes
from routes.transaction_routes import transaction_routes

# Register blueprints (similar to using routers in Express)
app.register_blueprint(book_routes, url_prefix='/books')
app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(transaction_routes, url_prefix='/transactions')

# Define a route for the root URL "/"
@app.route('/')
def home():
    return jsonify(message="Welcome to our Bookstore/Library Management System!"), 200

# Catch unhandled requests (404 Not Found)
@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not Found"), 404

# Global error handler (500 Internal Server Error)
@app.errorhandler(500)
def server_error(error):
    return jsonify(error="Internal Server Error"), 500

# Start the server
if __name__ == '__main__':
    # Use PORT environment variable if it exists, otherwise default to 3000
    PORT = int(os.getenv('PORT', 3000))
    app.run(debug=True, port=PORT)
