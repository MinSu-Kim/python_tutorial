import requests
import json

url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)
print(type(r.text), r.text)

json_to_dict = json.loads(r.text)
print(type(json_to_dict), json_to_dict)

r = requests.get(url)
json_to_dict = r.json()
print(type(json_to_dict), json_to_dict)

json_to_dict = requests.get(url).json()
type(json_to_dict)

print(json_to_dict["iss_position"])
print(json_to_dict["iss_position"]["latitude"])
print(json_to_dict["iss_position"]["longitude"])
print(json_to_dict["message"])
print(json_to_dict["timestamp"])