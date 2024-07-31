#!/usr/bin/env python3
"""Module for encrypting passwords."""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.
    
    Args:
        password: The password to hash.
    
    Returns:
        A salted, hashed password as a byte string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.
    
    Args:
        hashed_password: The hashed password.
        password: The password to check.
    
    Returns:
        True if the password is valid, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))
