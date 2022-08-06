import json
import requests

url = "https://api.github.com/rate_limit"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

response_dict = r.json()

with open("rate_limit.json", "w") as f:
    json.dump(response_dict, f, indent=4)