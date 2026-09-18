import requests

# Request an endpoint that intentionally returns HTTP 404.
response1 = requests.get("https://httpbin.org/status/404")

# Inspect the basic HTTP response.
print("Status:", response1.status_code)
print("Reason:", response1.reason)
print("Headers:", response1.headers)
print("OK?:", response1.ok)

# raise_for_status() does nothing for successful responses,
# but raises requests.exceptions.HTTPError for unsuccessful ones.
try:
    response1.raise_for_status()
except requests.exceptions.HTTPError as error:
    print("Raise for Status Failed")
    print("Error:", error)
    print("Response:", error.response)
    print("Response Status:", error.response.status_code)

    # Exploration notes:
#
# response1.raise_for_status
#     References the method without executing it.
#     I used this as a preview/inspection of the method.
#
# response1.raise_for_status()
#     Calls the method and raises HTTPError for unsuccessful responses.
#
# type(error)
#     Shows the exception's type.
#
# dir(error)
#     Shows the attributes and methods available on the exception.
#
# error.response
#     Gives access to the original Response object associated with the exception.
# ---------------------------------------------------------------------------------------
# Successful responses do not raise an HTTPError.
success_response = requests.get("https://httpbin.org/status/200")

print("\nSuccessful response:")
print("Status:", success_response.status_code)
print("Reason:", success_response.reason)
print("OK?:", success_response.ok)

try:
    success_response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print("This should not execute:", error)
else:
    print("No HTTPError raised.")

    # JSON notes:
#
# response1.json()
#     Attempts to deserialize the response body as JSON.
#     It does NOT mean "give me whatever the API returned."
#     If the body is empty or isn't valid JSON, it raises a JSONDecodeError.
#
# A response can therefore have:
#     - a valid HTTP status
#     - headers
#     - an empty body
#     - no JSON to decode