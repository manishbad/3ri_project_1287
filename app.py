# app.py
# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask application
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for resources like templates and static files.
app = Flask(__name__)

# Define a route for the root URL ("/") of the application
# The @app.route() decorator tells Flask what URL should trigger our function.
@app.route('/')
def hello_world():
    """
    This function is called when a user accesses the root URL.
    It returns a simple "Hello, World!" string.
    """
    return 'Hello, World!'

# Check if the script is executed directly (not imported)
# This is standard Python practice to make code reusable.
if __name__ == '__main__':
    # Run the application on a local development server.
    # debug=True will automatically reload the server when you make changes
    # and show you helpful error messages in the browser.
    # host='0.0.0.0' makes the server accessible from any device on your network.
    app.run(debug=True, host='0.0.0.0')

