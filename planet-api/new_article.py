import requests

planet_id = '999BB908-B79A-4C89-8DA6-1339BDFCE03E'

# Define the URL to send the request to
url = f"http://127.0.0.1:8086/v0/planets/my/{planet_id}/articles"

# Define the files to be uploaded
files = {'attachment': ('example.jpeg', open('example.jpeg', 'rb'), 'image/jpeg', {'Expires': '0'})}

# Define the additional form data
content = """
Content can be written in Markdown format.

- Hello
- World
"""

data = {
    'title': 'Title',
    'content': content
}

# Send the multipart POST request
response = requests.post(url, files=files, data=data)

# Print the response from the server
print(response.status_code)
print(response.text)
