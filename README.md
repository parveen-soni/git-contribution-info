# Git Contribution Repo

This repository contains a Python script designed to analyze user contributions (commit counts) across all repositories within a specified GitHub organization. 

## Features

- Fetches all repositories within a given organization.
- Retrieves the total commit count for a specified user in each repository.
- Summarizes the contributions and provides a breakdown by repository.

## Getting Started

### Prerequisites

- Python 3.6 or higher.
- `requests` library installed. You can install it using:
  ```bash
  pip3 install requests
  ```
- A valid GitHub personal access token with access to the target organization.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/git-contribution-repo.git
   cd git-contribution-repo
   ```
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
   *(Create a `requirements.txt` with `requests` if needed.)*

### Configuration

1. Open the `git_info.py` file.
2. Set the following variables:
   - `TOKEN`: Your GitHub personal access token.
   - `ORG_NAME`: The name of the target GitHub organization.
   - `USERNAME`: The username of the contributor whose commits you want to count.

Example:
```python
TOKEN = "your_personal_access_token"
ORG_NAME = "your_organization_name"
USERNAME = "contributor_username"
```

## Usage

Run the script to fetch and summarize contributions:
```bash
python git_info.py
```

### Output

- **Total Contributions**: The total number of commits made by the user across all repositories.
- **Repository Breakdown**: A list of repositories with their respective commit counts.

Example:
```
Total contributions by parveen-soni: 150
Repository: repo1, Commits: 50
Repository: repo2, Commits: 100
```

## Code Overview

The script is organized into the following steps:

1. **Fetch Repositories**: Uses GitHub's API to retrieve all repositories in the organization.
2. **Count Commits**: Loops through each repository and counts commits by the specified user using paginated API calls.
3. **Summarize Contributions**: Calculates the total contributions and displays a detailed breakdown.

## License

This project is open-source software licensed under the terms of the [GPL-3.0 license](https://github.com/parveen-soni/git-contribution-info/blob/main/LICENSE).

## Author

**Parveen Soni**  
[GitHub Profile](https://github.com/parveen-soni)

---

**Disclaimer**: Ensure that you use a secure and valid GitHub token, and avoid hardcoding sensitive credentials in the code.
