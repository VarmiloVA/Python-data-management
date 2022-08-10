from operator import itemgetter

import requests

# Does a request to the API
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}\n")

# Examine the data
submissions_ids = r.json()
submission_dicts = []
for submission_id in submissions_ids[:30]:
    # Does a individual request to the API for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tStatus: {r.status_code}")
    response_dict = r.json()

    # Creates a dict for each article
    try:
        submission_dict = {
            'title': response_dict['title'],
            'link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants']
        }
    except KeyError: #It's caused when there isn't descendants
        submission_dict = {
            'title': response_dict['title'],
            'link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': 0
        }

    submission_dicts.append(submission_dict)

submissions_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"\nDiscussion link: {submission_dict['link']}")
    print(f"\nComments: {submission_dict['comments']}\n")