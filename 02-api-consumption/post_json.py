import requests

stats = {'name': "Dan", 'course': "api-engineering", 'Skill': "API engineering"}

sending = requests.post("https://httpbin.org/post", json=stats)

data = sending.json()
print ("Status: ", sending.status_code)
print ("Response data: ", data.get("url"))
print(data.keys())
extract = data.get("json")
print(extract)
print(extract.get('name'))
print(extract.get('course'))
print(extract.get('Skill'))
print(data.get("headers"))