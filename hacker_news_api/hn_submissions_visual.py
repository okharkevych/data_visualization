from operator import itemgetter

import requests
from plotly import offline

# Make an API call and save the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Process each submission data
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {r.status_code}')
    response_dict = r.json()

    # Create a dict for each submission that
    # has comments-related key in data
    if 'descendants' in response_dict.keys():
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submission_id}',
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True
)

submission_links, comments_nums = [], []
for submission_dict in submission_dicts:
    submission_name = submission_dict['title']
    submission_url = submission_dict['hn_link']
    submission_link = f'<a href="{submission_url}">{submission_name}</a>'
    submission_links.append(submission_link)

    comments_nums.append(submission_dict['comments'])

# Create visualization
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': comments_nums,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.7,
}]

my_layout = {
    'title': 'Most-Discussed Submissions on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Submission',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')
