import requests
import json

# Does a request to the API and saves the answer
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Examine the data
response_dicit = r.json()
readable_file  = 'data/readable_hn_data.json'
with open(readable_file, "w") as f:
    json.dump(response_dicit, f, indent=4)
    print("Succes!")