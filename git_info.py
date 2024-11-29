#
#  Copyright (c) 2024.
#  Author Name: Parveen Soni
#  Copyright disclaimer: open source software
#  FileName: git_info.py
#

import requests
# function to get count of all commit counts for a given repository
# request will be called multiple times with page size of 100
def get_all_commits(org_name, repo_name, username, headers):
    commits = []
    commits_url = f"https://api.github.com/repos/{org_name}/{repo_name}/commits"
    params = {"author": username, "per_page": 100}  # Increase per page limit to 100
    while commits_url:
        response = requests.get(commits_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error fetching commits for {repo_name}: {response.status_code}, {response.json()}")
            break
        commits.extend(response.json())
        commits_url = response.links.get('next', {}).get('url')  # Follow the 'next' page link
    return len(commits)

# Configuration
TOKEN = "ghp_QCQtZ7ASqGU5nSUD0Ilsfskdjfsdlkjfksdfkjsh"
ORG_NAME = "XYZ"
USERNAME = "parveen-soni"
headers = {"Authorization": f"token {TOKEN}"}

# Step 1: Get all repositories in the organization
repos_url = f"https://api.github.com/orgs/{ORG_NAME}/repos"
repos = []
while repos_url:
    response = requests.get(repos_url, headers=headers)
    response_data = response.json()
    repos.extend(response_data)
    repos_url = response.links.get('next', {}).get('url')  # Handle pagination

# Step 2: Fetch contributions for the user in each repository
contributions = {}
for repo in repos:
    #if(repo['name'] =='spring'):
    repo_name = repo['name']
    #print (f'Fetching contributions for {repo_name}')
    commits_url = f"https://api.github.com/repos/{ORG_NAME}/{repo_name}/commits?author={USERNAME}"
    contributions[repo_name] = get_all_commits(ORG_NAME, repo_name, USERNAME, headers)


# Step 3: Summarize contributions
total_contributions = sum(contributions.values())
print(f"Total contributions by {USERNAME}: {total_contributions}")

# Step 4: Print repository names and their respective commits
for repo, count in contributions.items():
    print(f"Repository: {repo}, Commits: {count}")
