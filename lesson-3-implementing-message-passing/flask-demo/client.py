import requests

API_URL = "http://localhost:7111"

# should return the default route"s output
result = requests.get(API_URL)
if result.status_code == 200:
    print(result.json())

# should return the demo path example
result = requests.post(API_URL + "/demo/myPath?param_demo=myParam", json={"key": "value"}, headers={"header_demo": "myHeader"})
if result.status_code == 200:
    print(result.json())

# should return the api example item
result = requests.get(API_URL + "/api/items/1")
if result.status_code == 200:
    print(result.json())

# should return the api example new item
result = requests.post(API_URL + "/api/items/1", json={"name": "new_item"})
if result.status_code == 200:
    print(result.json())
