#!/usr/bin/env python3
"""Module for filtering sensitive information from log messages."""

import re
import logging
import mysql.connector
import os
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated.
    
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all fields in the log line
    
    Returns:
        The obfuscated log message
    """
    pattern = r'({})=[^{}]*'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the specified record as text."""
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    
    logger.addHandler(stream_handler)
    
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    
    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main():
    """Main function to retrieve and display filtered user data"""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    
    for row in cursor:
        message = "; ".join(f"{field}={value}" for field, value in zip(cursor.column_names, row))
        logger.info(message)
    
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
