from flask import Flask, request, jsonify # we also import 'render_template' to render HTML templates
import pymongo # we import 'datetime' to work with date and time in our API endpoints
from dotenv import load_dotenv # we import 'load_dotenv' to load environment variables from a .env file
from urllib.parse import quote_plus
import os # we import 'os' to access environment variables
# from pymongo import MongoClient # we import 'MongoClient' to connect to our MongoDB
import pymongo # we import 'pymongo' to connect to our MongoDB database and perform database operations
from pymongo import MongoClient
from bson import ObjectId

load_dotenv() # we call 'load_dotenv()' to load environment variables from the .env file

username = quote_plus(os.getenv("MONGO_USER"))
password = quote_plus(os.getenv("MONGO_PASS"))

MONGO_URI = f"mongodb+srv://{username}:{password}@rk.9hyvp36.mongodb.net/?appName=RK"

client = MongoClient(MONGO_URI)

db = client["test"]   # database
collection = db["flask_tutorial"]  # collection

app = Flask(__name__)

@app.route('/submit', methods=['POST']) # we specify that this endpoint only accepts POST requests
def submit():
    # form_data = request.form.to_dict()
    form_data = dict(request.form) # we can get all form data as a dictionary using 'request.form.to_dict()''
    result = collection.insert_one(form_data)
    form_data["_id"] = str(result.inserted_id)
    return form_data    


@app.route('/users')
def get_users():
    users = list(collection.find()) # we retrieve all documents from the 'users' collection and convert the cursor to a list
    for user in users:
        user['_id'] = str(user['_id']) # we convert the ObjectId to a string for JSON serialization
    print ('Retrieved users from database:', users) # we print the retrieved users to the console for debugging
    for user in users:
        del user['_id'] # we remove the '_id' field from each user document before returning the response, since it's not needed in the API response
    # return {'users': users} # we return the list of users as a JSON response
    data = {'users': users}
    return jsonify(data)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True) # we specify the host and port for the Flask app to run on, and enable debug mode for easier development and troubleshooting