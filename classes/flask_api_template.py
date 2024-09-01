# api_template.py
"""
Generic API Template using Flask
--------------------------------

This script sets up a basic API using Flask, a popular Python web framework.
It defines a generic API class with endpoints that can be extended as needed.

Quick Reference for Expanding the API:
--------------------------------------

1. **Adding New Routes:**
   - To add a new endpoint, define a new route inside the `setup_routes` method.
   - Example:
     @self.app.route('/new_endpoint', methods=['GET'])
     def new_endpoint():
         # Define the logic for this endpoint
         return jsonify({"message": "This is a new endpoint"})

2. **Encapsulating Further with New Classes:**
   - Create additional classes to handle different parts of the API (e.g., separate controllers for different resources).
   - Example:
     class UserAPI:
         def __init__(self, app):
             self.app = app
             self.setup_user_routes()

         def setup_user_routes(self):
             @self.app.route('/users', methods=['GET'])
             def get_users():
                 # Logic for handling users
                 return jsonify({"users": []})

3. **Adding New Methods:**
   - Define new methods within the GenericAPI class or any new class to encapsulate functionality.
   - Example:
     def process_data(self, data):
         # Perform operations on data
         return processed_data

4. **Integrating Database:**
   - Use SQLAlchemy or another ORM to interact with a database.
   - Example:
     from flask_sqlalchemy import SQLAlchemy
     db = SQLAlchemy(self.app)

5. **Implementing Error Handling:**
   - Add error handlers to manage exceptions and return appropriate HTTP status codes.
   - Example:
     @self.app.errorhandler(404)
     def not_found_error(error):
         return jsonify({"error": "Not Found"}), 404

6. **Adding Middleware:**
   - Use middleware functions for cross-cutting concerns like logging, authentication, etc.
   - Example:
     @self.app.before_request
     def before_request_func():
         # Logic before every request

7. **Authentication and Authorization:**
   - Integrate JWT, OAuth2, or another method to protect routes.
   - Example:
     from flask_jwt_extended import JWTManager

     jwt = JWTManager(self.app)

Usage:
    1. Install Flask if not already installed: pip install flask
    2. Run the script: python api_template.py
    3. Access the API at http://127.0.0.1:5000/

Example:
    You can use this template to build your own API by extending the GenericAPI class.
"""

from flask import Flask, jsonify, request

class GenericAPI:
    def __init__(self, name):
        """
        Initialize the Flask application.

        :param name: The name of the Flask application.
        """
        self.app = Flask(name)
        self.setup_routes()

    def setup_routes(self):
        """
        Define the routes for the API.
        """
        @self.app.route('/', methods=['GET'])
        def index():
            """
            Default route for the API.

            :return: A JSON welcome message.
            """
            return jsonify({"message": "Welcome to the Generic API!"})

        @self.app.route('/data', methods=['GET'])
        def get_data():
            """
            Example GET endpoint to retrieve data.

            :return: A JSON object with sample data.
            """
            sample_data = {"id": 1, "name": "Sample Data", "description": "This is some sample data."}
            return jsonify(sample_data)

        @self.app.route('/data', methods=['POST'])
        def create_data():
            """
            Example POST endpoint to create data.

            :return: A JSON object with the created data.
            """
            data = request.json
            return jsonify(data), 201

        @self.app.route('/data/<int:data_id>', methods=['PUT'])
        def update_data(data_id):
            """
            Example PUT endpoint to update data.

            :param data_id: The ID of the data to update.
            :return: A JSON object with the updated data.
            """
            updated_data = request.json
            updated_data['id'] = data_id
            return jsonify(updated_data)

        @self.app.route('/data/<int:data_id>', methods=['DELETE'])
        def delete_data(data_id):
            """
            Example DELETE endpoint to delete data.

            :param data_id: The ID of the data to delete.
            :return: A JSON object indicating success.
            """
            return jsonify({"message": f"Data with ID {data_id} deleted successfully."})

    def run(self, host='127.0.0.1', port=5000):
        """
        Run the Flask application.

        :param host: The host address to run the app on.
        :param port: The port to run the app on.
        """
        self.app.run(host=host, port=port)

# Example usage:
if __name__ == "__main__":
    api = GenericAPI(__name__)
    api.run()
