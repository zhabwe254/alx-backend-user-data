# User Authentication Service

## Description
This project implements a user authentication service using Flask and SQLAlchemy. It provides functionality for user registration, login, logout, password reset, and profile management.

## Features
- User registration
- User login and session management
- Password hashing and verification
- Password reset functionality
- User profile retrieval
- RESTful API endpoints

## Requirements
- Python 3.7+
- Flask
- SQLAlchemy
- bcrypt

## Installation
1. Clone this repository:
git clone https://github.com/your-username/user-authentication-service.git
cd user-authentication-service
Copy
2. Install the required packages:
pip install flask sqlalchemy bcrypt
Copy
## File Structure
- `app.py`: Main Flask application
- `auth.py`: Authentication logic
- `db.py`: Database operations
- `user.py`: User model

## Usage
1. Start the Flask server:
python app.py
Copy
2. The server will start running on `http://0.0.0.0:5000/`

## API Endpoints
- `POST /users`: Register a new user
- `POST /sessions`: Log in a user
- `DELETE /sessions`: Log out a user
- `GET /profile`: Get user profile
- `POST /reset_password`: Request password reset
- `PUT /reset_password`: Update password

## Testing
To run the provided test cases:
python -m unittest test_auth.py

Author:

GIDEON HABWE
