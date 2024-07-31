# Personal Data Project

## Description
This project focuses on handling personal data securely in a Python application. It includes functionality for filtering sensitive information from log messages, secure logging practices, connecting to a MySQL database, and working with personal user data.

## Features
- Filtering sensitive information from log messages
- Custom logging formatter for data protection
- Secure database connection handling
- Password hashing and validation

## Requirements
- Ubuntu 18.04 LTS
- Python 3.7+
- MySQL 5.7+

## Installation

1. Clone the repository:
git clone https://github.com/your-username/alx-backend-user-data.git
cd alx-backend-user-data/0x00-personal_data
Copy
2. Install required packages:
pip3 install mysql-connector-python bcrypt
Copy
3. Set up the MySQL database:
mysql -u root -p < main.sql
Copy
## Usage

1. Set the required environment variables:
export PERSONAL_DATA_DB_USERNAME=your_username
export PERSONAL_DATA_DB_PASSWORD=your_password
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=your_database_name
Copy
2. Run the main script:
python3 filtered_logger.py
Copy
3. For password hashing and validation:
python3 encrypt_password.py
Copy
## File Descriptions

- `filtered_logger.py`: Contains functions for logging and filtering personal data.
- `encrypt_password.py`: Includes functions for hashing and validating passwords.
- `main.sql`: SQL script to set up the test database.

## Author
GIDEON HABWE
