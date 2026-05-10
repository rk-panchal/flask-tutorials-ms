# Flask Frontend + Backend Project

A simple full-stack Python project using Flask for both frontend and backend services with MongoDB Atlas integration.

This project demonstrates:
- Flask API development
- Frontend and backend separation
- MongoDB Atlas integration
- REST API communication
- Form submission
- JSON responses
- Environment variable handling using `.env`

---

# Technologies Used

## Backend
- Python 3
- Flask
- MongoDB Atlas
- PyMongo
- python-dotenv

## Frontend
- Flask
- HTML Templates
- Requests library

---

# Project Structure

```bash
project/
│
├── backend/
│   ├── app.py
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── requirements.txt
│
└── README.md
```

---

# Features

## Backend Features
- MongoDB Atlas connection
- Save form data into MongoDB
- Retrieve user data from MongoDB
- REST API endpoints
- JSON response handling

## Frontend Features
- HTML page rendering
- Submit form data to backend API
- Fetch user data from backend API
- Display API responses

---

# Installation

## 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd <project-folder>
```

---

# Create Virtual Environment

```bash
python3 -m venv venv
```

Activate virtual environment:

## Linux / Mac

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install flask pymongo python-dotenv requests
```

---

# MongoDB Atlas Setup

Create a free cluster using:

[MongoDB Atlas](https://www.mongodb.com/atlas?utm_source=chatgpt.com)

---

# Backend Environment Variables

Create `.env` file inside `backend/`

```env
MONGO_USER=your_username
MONGO_PASS=your_password
```

---

# Backend Application

## Run Backend Server

Navigate to backend folder:

```bash
cd backend
```

Run application:

```bash
python3 app.py
```

Backend runs on:

```bash
http://localhost:8000
```

---

# Frontend Application

## Run Frontend Server

Open another terminal:

```bash
cd frontend
```

Run application:

```bash
python3 app.py
```

Frontend runs on:

```bash
http://127.0.0.1:5000
```

---

# Backend API Endpoints

---

## Submit User Data

### Endpoint

```bash
POST /submit
```

### Description

Stores form data into MongoDB Atlas.

---

## Get Users

### Endpoint

```bash
GET /users
```

### Description

Retrieves all users from MongoDB collection.

### Sample Response

```json
{
  "users": [
    {
      "name": "Ravinder",
      "email": "test@gmail.com"
    }
  ]
}
```

---

# Frontend Routes

---

## Home Page

### Endpoint

```bash
/
```

### Description

Renders HTML home page with:
- Current day
- Current date/time

---

## Submit Form

### Endpoint

```bash
POST /submit
```

### Description

Sends form data to backend API.

---

## Get Data

### Endpoint

```bash
GET /get_data
```

### Description

Fetches data from backend `/users` API.

---

# MongoDB Connection

MongoDB connection is created using:

```python
MongoClient(MONGO_URI)
```

MongoDB Atlas credentials are securely loaded from `.env`.

---

# Important Concepts Used

- Flask Routing
- REST APIs
- Frontend-Backend Communication
- MongoDB Integration
- Environment Variables
- JSON APIs
- Form Handling
- HTTP Requests
- API Architecture

---

# ObjectId Handling

MongoDB returns `_id` as `ObjectId`.

Before returning JSON response:

```python
user['_id'] = str(user['_id'])
```

This prevents JSON serialization errors.

---

# Run Multiple Services

This project uses:
- Backend service on port `8000`
- Frontend service on port `5000`

Frontend communicates with backend using:

```python
requests.get()
requests.post()
```

---

# Future Improvements

- Add Update/Delete APIs
- Add User Authentication
- Add Docker Support
- Add JWT Authentication
- Deploy on AWS
- Add React frontend
- Add Logging
- Add API validation

---

# Author

Ravinder Kumar
