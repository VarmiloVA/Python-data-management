import requests

#Does a requests to the github API
url = "https://api.github.com/search/repositories?q=language:brainfuck&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"\nStatus code: {r.status_code}")

#Saves the response
response_dict = r.json()
#Process the response
print(f"Total repositories: {response_dict['total_count']}")
print(response_dict.keys(), "\n")