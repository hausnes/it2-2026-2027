# Eksempel frå https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/

# Import the necessary module
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
PASSORD = os.getenv('PASSORD')

# Example usage
print(f'PASSORD: {PASSORD}')