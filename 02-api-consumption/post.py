import requests

payload = {
    "title": "My test post",
    "body": "Testing POST",
    "userId": 3
}
url = "https://jsonplaceholder.typicode.com/posts"
 

response = requests.post(url=url, json=payload
)

print(response.status_code)
print(response.json())
print(response.headers)
print(response.url)