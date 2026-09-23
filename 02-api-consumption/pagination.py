import requests
import json


params = {"_page": 1, "_limit": 5}
records = []
rec_count = []
counter = 0
response1 = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
rec_limit = params.get("_limit")
data = response1.json()

# add to the records
for x in data:
    records.append(x.get("id"))
    counter += 1
    rec_count.append(counter)
print("page:", params["_page"])
print(rec_count)

####  debugging
#records = data[0].get("userId")
#print ("page: ", extract)
#print(type(data))
####  end

while len(records) == rec_limit:
    params["_page"] += 1
    print("page:", params["_page"])
    records = []
    rec_count = []
    response1 = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
    data = response1.json()
    for x in data:
        # add to the records
        records.append(x.get("id"))
        counter += 1
        rec_count.append(counter)
    print(rec_count)

# print(json.dumps(data, indent=4)) #for diagnostics and review. Employ this code for prettier JSON output.
