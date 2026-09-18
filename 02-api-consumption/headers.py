import requests

headers1 = {'X-Client-Name' : 'api-engineering-lab'}

response1 = requests.get("https://httpbin.org/headers", headers=headers1)
data = response1.json()
print("Response Headers:", response1.headers)
print("Response Body:", data)

extract = data.get("headers")
print("Request Headers Received by Server:", extract)
print("X-Client-Name:", extract.get("X-Client-Name"))