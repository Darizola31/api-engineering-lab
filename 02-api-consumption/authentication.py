import requests
import os

# verfiy the key is not empty
def return_key():
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError("Environment variable is missing or empty")
    return api_key

def authenticate(expected_key, received_key):
    if expected_key == received_key:
        return 200
    else:
        return 401

#put your functions here!
api_key = return_key()


#key variables
headers = {'X-API-Key': api_key}


#from the server
response1 = requests.get("https://httpbin.org/headers", headers= headers)
data = response1.json()
extract = data.get("headers")
#print("API Key Present:", "X-Api-Key" in extract)
#print("Response Status:", response1.status_code)

#variable check
expected = "super-secret-demo-key"
returned = extract.get("X-Api-Key")
result = authenticate(expected, returned)

print(result)