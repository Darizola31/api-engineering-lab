import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "body": "This is my patched body"
}

response = requests.patch(url, json=payload)

print(response.status_code)
print(response.json())
print(response.headers)
