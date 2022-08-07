import requests

from plotly.graph_objs import Bar
from plotly import offline

# Does a request to the API
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Saves the answer given by the API in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Process the answer
repo_dicts = response_dict['items']

repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts: #Getting the needed data for plotly
    repo_owner = repo_dict['owner']['login']
    if len(repo_dict['description']) > 255:
        repo_description = 'Too long'
    elif len(repo_dict['description']) == 0:
        repo_description = 'There is no description'
    else:
        repo_description = repo_dict['description']

    repo_link = repo_dict['html_url']

    repo_name = f"<a href='{repo_link}'>{repo_dict['name']}</a>"
    label = f"Owner: {repo_owner}<br />Description: {repo_description}"

    labels.append(label)
    repo_names.append(repo_name)
    stars.append(repo_dict['stargazers_count'])

data = [{
    'x': repo_names,
    'y': stars,
    'type': 'bar',
    'orientation': 'v',
    'hovertext': labels,
    'hoverinfo': 'text',
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
    'opacity': 0.5,
    }]

data[0]['hovertext'] = labels

layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 20}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 20}
    }
}

# Visualize the data
fig = {
    'data': data, 
    'layout': layout, 
    }
offline.plot(fig, filename='python_repos.html')