import requests
import json


records = []

page = int(input("Enter page number: "))
limit = int(input("How many posts per page? "))

params = {
    "userId": 3,
    "_page": page,
    "_limit": limit
    }

response1 = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
    )

print(response1.url)

data = response1.json()
for x in data:
    records.append(x.get("id"))

print("page:", page)
print("records:", len(data))
print("IDs:", records)
