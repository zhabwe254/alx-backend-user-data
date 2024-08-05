#!/usr/bin/env python3
"""
Authentication module
"""
from typing import TypeVar
from flask import request

User = TypeVar('User')

class Auth:
    """
    Authentication class
    """
    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """
        Retrieves the current user from the request
        """
        return None

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """
        Determines if a path requires authentication
        """
        if not path or not excluded_paths:
            return True
        return not any(path.startswith(ep) for ep in excluded_paths)

