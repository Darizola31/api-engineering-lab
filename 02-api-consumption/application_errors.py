import requests

response1 = requests.get("https://httpbin.org/json")
data = response1.json()
print(data)
extract = data.get("success")
print(extract)
