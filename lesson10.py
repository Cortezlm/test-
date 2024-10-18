# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:")

# Prompt for the URL
url = input("Please type the destination URL you like to use;")
# Display the URL
print(f"you enter the url: {url}")
import requests

# Step 2: Input HTTP Method
http_method = input("Please select an HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Step 3: Display request details
print(f"\nRequest Details:\nURL: {url}\nHTTP Method: {http_method}")
confirmation = input("Do you want to proceed with this request? (yes/no): ")

# Step 4: Execute the request if confirmed
if confirmation.lower() == 'yes':
    if http_method == 'GET':
        response = requests.get(url)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    # Add other methods as needed
else:
    print("Request cancelled.")
