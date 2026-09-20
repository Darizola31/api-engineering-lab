import requests
try:
    response1 = requests.get("https://httpbin.org/delay/10", timeout=2)
except requests.exceptions.ReadTimeout:
    print("Request timed out")
