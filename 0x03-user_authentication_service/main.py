#!/usr/bin/env python3
"""
Main file to test the entire implementation
"""

from auth import Auth

auth = Auth()

# Test user registration
try:
    user = auth.register_user("user@example.com", "SecurePass")
    print("User created:", user.email)
except ValueError as err:
    print(err)

# Test valid login
if auth.valid_login("user@example.com", "SecurePass"):
    print("Login valid")
else:
    print("Login invalid")

# Test invalid login
if auth.valid_login("user@example.com", "WrongPass"):
    print("Login valid")
else:
    print("Login invalid")

# Test session creation
session_id = auth.create_session("user@example.com")
print("Session ID:", session_id)

# Test getting user from session ID
user = auth.get_user_from_session_id(session_id)
if user:
    print("User from session:", user.email)

# Test session destruction
auth.destroy_session(user.id)
user = auth.get_user_from_session_id(session_id)
if user is None:
    print("Session destroyed")
