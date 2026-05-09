# flask-tutotials
# Flask Learning Project

A simple Flask application created for learning Flask basics, API creation, routing, templates, request handling, and arithmetic operations.

---

# Features

- Home page with current day and time
- About page
- Dynamic API routes
- Arithmetic operation APIs
- Query parameter handling
- JSON responses
- HTML template rendering using Jinja2
- Current server time API

---

# Technologies Used

- Python 3
- Flask
- HTML
- Jinja2 Templates

---

# Project Structure

```bash
project/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd <project-folder>
```

## 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Linux / Mac

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Flask

```bash
pip install flask
```

---

# Run the Application

```bash
python app.py
```

Application will run on:

```bash
http://127.0.0.1:5000
```

---

# API Endpoints

---

## Home Page

### URL

```bash
/
```

### Description

Displays:
- Current day
- Current date and time

---

## About Page

### URL

```bash
/about
```

### Response

```text
This is the about page of my Flask app
```

---

# Dynamic API Endpoint

## URL

```bash
/api/<name>
```

### Example

```bash
/api/satvik
```

### Conditions

- Name length less than 3 → Error
- Name = admin → Access denied
- Name length greater than 10 → Success message
- Otherwise → Basic greeting message

---

# Arithmetic API

## URL

```bash
/api/<operation>/<num1>/<num2>
```

### Supported Operations

- add
- subtract
- multiply
- divide

### Examples

#### Addition

```bash
/api/add/5/10
```

#### Subtraction

```bash
/api/subtract/10/5
```

#### Multiplication

```bash
/api/multiply/5/10
```

#### Division

```bash
/api/divide/10/2
```

---

# JSON API

## URL

```bash
/api
```

### Sample Response

```json
{
  "name": "Flask API",
  "version": "1.0",
  "description": "This is a simple API endpoint that returns JSON data."
}
```

---

# Query Parameter API

## URL

```bash
/api_request?name=satvik&age=25
```

### Description

Checks whether the user age is greater than 20.

### Example Response

```json
{
  "message": "Hello, satvik! You are 25 years old. You can use this site",
  "name": "satvik",
  "age": 25
}
```

---

# Current Time API

## URL

```bash
/time
```

### Sample Response

```json
{
  "current_time": "2026-05-09 10:30:45"
}
```

---

# Template Rendering

The application uses:

```python
render_template('index.html')
```

to render HTML pages from the `templates` folder.

---

# Debug Mode

Application runs in debug mode:

```python
app.run(debug=True)
```

Benefits:
- Auto reload on code changes
- Detailed error messages during development

---

# Learning Concepts Covered

- Flask Routing
- Dynamic URLs
- Query Parameters
- JSON Responses
- Request Handling
- HTML Template Rendering
- File Structure in Flask
- Conditional Statements
- Basic API Development

---

# Author

Ravinder Kumar
