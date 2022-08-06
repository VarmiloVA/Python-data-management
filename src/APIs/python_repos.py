import requests

# Does a requests to the github API
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Saves the response
response_dict = r.json()
print(f"\nStatus code: {r.status_code}") # Status code: 200 OK

# Process the response
# print(f"Total repositories: {response_dict['total_count']}")
# print(response_dict.keys(), "\n")

# Saves the information of the repositories
print(f"Total repositories: {response_dict['total_count']}")
repos_dict = response_dict["items"]
print(f"Repositories returned: {len(repos_dict)}")

# Works with info from the first repo
print("\n\nSelected information about the top 10 best rated repositories:\n")
for repo in repos_dict[0:10]:
    print(f"Name: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}")
    print("\n")