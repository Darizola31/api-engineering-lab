#lesson 2.1 - api query attributes
import requests

params = {'name': "Dan", 'course': "api-engineering"}

response1 = requests.get("https://httpbin.org/get", params)

data = response1.json()
print ("Status: ", response1.status_code)
print ("Response data: ", data.get("url"))
print(data.keys())
extract = data.get("args")
print(extract.get('name'))
print(extract.get('course'))