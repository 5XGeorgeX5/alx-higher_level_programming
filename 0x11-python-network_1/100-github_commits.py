#!/usr/bin/python3
"""takes yourusername and repo on GitHub and displays last 10 commits"""

if __name__ == "__main__":
    from sys import argv
    from requests import get

    response = get("https://api.github.com/repos/"
                   f"{argv[2]}/{argv[1]}/commits?per_page=10")
    commits = response.json()
    for commit in commits:
        name = commit.get('commit').get('author').get('name')
        print(f"{commit.get('sha')}: {name}")
