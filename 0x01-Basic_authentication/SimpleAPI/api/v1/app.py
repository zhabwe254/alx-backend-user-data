#!/usr/bin/env python3
"""
Main module for the API
"""
from flask import Flask, request, abort
from flask_cors import CORS
import os

# Import the relevant Auth class based on AUTH_TYPE
auth = None

if os.getenv('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif os.getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

app = Flask(__name__)
CORS(app)

@app.before_request
def before_request():
    """
    Handles requests before they are processed
    """
    if auth is None:
        return
    
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    
    if request.path not in excluded_paths:
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)

@app.route('/api/v1/status', methods=['GET'])
def status():
    """
    Returns the status of the API
    """
    return {'status': 'OK'}

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """
    Returns unauthorized error message
    """
    return {'error': 'Unauthorized'}, 401

@app.route('/api/v1/forbidden', methods=['GET'])
def forbidden():
    """
    Returns forbidden error message
    """
    return {'error': 'Forbidden'}, 403

if __name__ == '__main__':
    app.run(host=os.getenv('API_HOST', '0.0.0.0'), port=int(os.getenv('API_PORT', 5000)))
