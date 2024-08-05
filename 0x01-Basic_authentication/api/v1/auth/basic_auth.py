#!/usr/bin/env python3
"""
Basic authentication module
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64

class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 string to a UTF-8 string
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> User:
        """
        Retrieves the User instance from email and password
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        user = User.search(user_email)
        if not user:
            return None
        user = user[0]
        if user.is_valid_password(user_pwd):
            return user
        return None

    def current_user(self, request=None) -> User:
        """
        Retrieves the User instance from the request
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        base64_auth_header = self.extract_base64_authorization_header(auth_header)
        if base64_auth_header is None:
            return None
        decoded_auth_header = self.decode_base64_authorization_header(base64_auth_header)
        if decoded_auth_header is None:
            return None
        email, pwd = self.extract_user_credentials(decoded_auth_header)
        return self.user_object_from_credentials(email, pwd)
