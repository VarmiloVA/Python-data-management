import requests

# Does a request to the API
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#Documentation for api.github.com is here: https://docs.github.com/es/rest
headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Saves the answer given by the API in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Process the answer
repo_dicts = response_dict['items']

# Explores the most starred repositories
print("\nSelected info about the top 10 most starred repo:")
for repo_dict in repo_dicts[0:10]:
    print(f"\nName: {repo_dict['name']}")
    print(f"\nOwner: {repo_dict['owner']['login']}")
    print(f"\nStars: {repo_dict['stargazers_count']}")
    print(f"\nDescription: {repo_dict['description']}")
    print(f"\nForks: {repo_dict['forks_count']}")
    print("\n")