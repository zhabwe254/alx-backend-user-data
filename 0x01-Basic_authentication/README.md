# Basic Authentication API

This project implements a Basic Authentication system for a RESTful API using Python and Flask.

## Project Structure
0x01-Basic_authentication/
├── api/
│   ├── v1/
│   │   ├── app.py
│   │   ├── views/
│   │   │   ├── index.py
│   │   │   └── users.py
│   │   └── auth/
│   │       ├── init.py
│   │       ├── auth.py
│   │       └── basic_auth.py
├── models/
│   ├── base.py
│   └── user.py
└── README.md
Copy
## Setup and Installation

1. Clone the repository:
git clone [repository-url]
cd 0x01-Basic_authentication
Copy
2. Install dependencies:
pip3 install -r requirements.txt
Copy
3. Run the API:
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
Copy
## Authentication Flow

This API uses Basic Authentication. The authentication flow is as follows:

1. The client sends a request with an `Authorization` header containing the Base64 encoded string of `username:password`.
2. The server decodes the Authorization header and extracts the credentials.
3. The server validates the credentials against the user database.
4. If valid, the request is processed. If invalid, an appropriate error response is sent.

## API Endpoints

- GET /api/v1/status/: Check API status
- GET /api/v1/unauthorized/: Test 401 error
- GET /api/v1/forbidden/: Test 403 error
- GET /api/v1/users/: List all users (requires authentication)

## Error Handling

- 401 Unauthorized: When authentication fails
- 403 Forbidden: When the user is authenticated but not allowed to access a resource

## Testing

You can test the API using curl commands. For example:
curl "http://0.0.0.0:5000/api/v1/status"
curl "http://0.0.0.0:5000/api/v1/unauthorized"
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic $(echo -n username:password | base64)"
Copy
Replace `username:password` with valid credentials.

## Author
GIDEON HABWE
