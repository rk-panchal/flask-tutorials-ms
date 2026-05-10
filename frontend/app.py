#from flask import Flask # need to import Flask class from the flask module to create a Flask application instance
# from flask import Flask, request # we also import 'request' to handle incoming request data in our API endpoints
from flask import Flask, render_template, request # we also import 'render_template' to render HTML templates
from datetime import datetime
import requests # we import 'requests' to make HTTP requests to our backend API

BACKEND_URL = 'http://localhost:8000' # we define the URL of our backend API,
app = Flask(__name__)

@app.route('/')
def home():
    # return 'Hello, Flask! Welcome to My Home page'
    day_of_week = datetime.now().strftime('%A') # we get the current day of the week using 'datetime.now()' and format it as a string using 'strftime()'
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # we get the current date and time and format it as a string
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time) # we render the 'index.html' template and pass the 'day_of

@app.route('/about')
def about():
    return 'This is the about page of my Flask app'
#/api/satvik
@app.route('/api/<name>') #we can pass a variable in the URL, in this case, 'name'

def api(name):
    print('api endpoint called with name:', name)
    # return ('This is a simple API endpoint.')
    length = len(name)
    
    if length < 3:
        return 'Name must be at least 3 characters long.', 400
    elif name.lower() == 'admin':
        return 'Access denied for admin user.', 403
    elif length > 10:
        return f'Hello, {name}! This is a simple API endpoint.'
    else:
        return 'Hello' + name + 'This is a test simple API endpoint.'

#/api/add/5/10
@app.route('/api/<p1>/<p2>/<p3>') 
def api_with_two_params(p1, p2, p3):
    print('api endpoint called with parameters:', p1, p2, p3)
    
    if p1 == 'add':
        result = int(p2) + int(p3)
    elif p1 == 'subtract':
        result = int(p2) - int(p3)
    elif p1 == 'multiply':
        result = int(p2) * int(p3)
    elif p1 == 'divide':
        if int(p3) == 0:
            return 'Error: Division by zero is not allowed.', 400
        else:
            result = int(p2) / int(p3)
    else:
        return 'Invalid operation. Use add, subtract, multiply, or divide.', 400
    
        

    return  {'result': result,
            'message': f'The {p1} result of {p2} and {p3} is {result}.'
            }

    # return f'Hello, {p1} and {p2}! This is a simple API endpoint.'
#/api
@app.route('/api')
def show_api_data():
    data = {
        'name': 'Flask API',
        'version': '1.0',
        'description': 'This is a simple API endpoint that returns JSON data.'
    }
    return data

#/api_request?name=satvik&age=12
@app.route('/api_request') # we specify that this endpoint only accepts POST requests
def show_request_data():
    name = request.values.get('name') # we can get query parameters from the request using 'request.args.get()'
    age = request.values.get('age')
    age = int(age) if age is not None else None # convert age to an integer if it's provided, otherwise set it to None
    if age > 20:
        response = {
            'message': f'Hello, {name}! You are {age} years old. You can use this site',
            'name': name,
            'age': age
        }
    else:
        response = {
        'message': f'Hello, {name}! You are {age} years old. You cannot use this site',
        'name': name,
        'age': age
    }
    return response

@app.route('/time')
def time():
    return {'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

@app.route('/submit', methods=['POST']) # we specify that this endpoint only accepts POST requests
def submit():
    form_data = dict(request.form) # we can get all form data as a dictionary using 'request.form.to_dict()''
    requests.post(f'{BACKEND_URL}/submit', data=form_data) # we send the form data to the backend API using 'requests.post()'
    return 'Form submitted successfully!' # we return a success message to the user after submitting the

@app.route('/get_data')
def get_data():
    response = requests.get(f'{BACKEND_URL}/users') # we make a GET request to the backend API to retrieve data using 'requests.get()'
    print('Response from backend API:', response.json()) # we print the response object to the console for debugging
    data = response.json() # we parse the JSON response from the backend API using 'response.json()' and store it in a variable called 'data'
    data['view']='frontend' # we add a 'view' key to the response dictionary to indicate that this data is being returned from the frontend API endpoint
    return data # we return the JSON response from the backend API to the frontend, which can be used to display the data on the webpage

if __name__ == '__main__':
    app.run(debug=True) 