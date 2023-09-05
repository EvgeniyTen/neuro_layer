import requests

# Define the URL of your FastAPI server
url = "http://localhost:8000/sendMessage"  # Replace with the actual URL where your FastAPI server is hosted

# Define the message you want to send
message = "Hello, FastAPI!"

# Create a dictionary with the message
data = {"text": message}

# Send a POST request to the URL with the message data
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    response_data = response.json()
    print("Response:", response_data)
else:
    print("Error:", response.text)
