import requests

# Make an API call and save the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Save the API response to a variable
response_dict = r.json()
print(f'Total repositories: {response_dict["total_count"]}')

# Explore information regarding repositories
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f'\nName: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repository: {repo_dict["html_url"]}')
    print(f'Created: {repo_dict["created_at"]}')
    print(f'Updated: {repo_dict["updated_at"]}')
    print(f'Description: {repo_dict["description"]}')
