import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "id": 101,
    "title": "new title"
}
#put function

response = requests.put(url, json= payload)

print(response.status_code)
print(response.text)
print(response.headers)


