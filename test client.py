import requests

# Define the Flask server URL
url = "http://127.0.0.1:5000/wordcount"

# Sample text input
data = {
    "text": "hello world\nhello Flask\nhello threading\nword count test"
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())