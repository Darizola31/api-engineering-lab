import requests
import json

base = "https://jsonplaceholder.typicode.com"
path = "/posts/1"
timeout = 3
headers= {}

def call(method, path, payload=None, timeout=timeout):
    response = requests.request(method, base+path, json=payload, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response
 
try:
    response1 = call("GET", path)
except requests.exceptions.HTTPError as error:
    print("Not Found Page Exception:", error)
except requests.exceptions.Timeout as error:
    print("Timeout Error")
else:
    print(json.dumps(response1.json(), indent=4, sort_keys=True))
    print(response1.status_code)
#connection errors.
