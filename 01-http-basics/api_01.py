import requests

response1 = requests.get("https://httpbin.org/get")
data = response1.json()
print ("Status: ", response1.status_code)
print ("Response data: ", data.get("url"))

### print(dir(response1))
####print (dir(data))