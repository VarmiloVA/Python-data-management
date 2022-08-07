import requests
from plotly.graph_objs import Bar
from plotly import offline

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

repo_links, labels, stars = [], [], []
for repo_dict in repos_dict:
    stars.append(repo_dict["stargazers_count"])
    repo_url = repo_dict["html_url"]
    repo_link = str(f"<a href='{repo_url}'>{name}</a>")
    repo_links.append(repo_link)

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br/>{description}"
    labels.append(label)

# Does the visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='python_repos.html')
