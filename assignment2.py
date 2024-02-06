import re

# Define regex patterns for username and password
username_pattern = r"^[a-zA-Z\s]+$"  # since it is a name string only
password_pattern = r"^\d{4}$"  # 4-digit PIN

# Initialize the maximum number of login attempts
max_attempts = 5

# Initialize the attempt counter
attempts = 0

# Nested loop to handle login attempts
while attempts < max_attempts:
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your 4-digit PIN: ")

    match1= re.search(username_pattern, username)
    match2= re.search(password_pattern, password)

    # Validate username and password using regex patterns
    if match1 and match2:
        print("Welcome to GTST Company!")
        break  # Exit the loop if successful login
    else:
        print("Incorrect Login! Please try again.")

    attempts += 1

# If all attempts are exhausted, display the limit message
if attempts == max_attempts:
    print("Sorry, you are limited!")
