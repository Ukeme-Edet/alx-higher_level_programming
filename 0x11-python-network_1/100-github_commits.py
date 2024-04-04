#!/usr/bin/python3
"""
Python script that takes a Github repository and user credentials (username and
password) and uses the Github API to display the last 10 commits
"""


def main():
    """
    Main function for the script
    """

    import requests
    from sys import argv

    username = argv[1]
    repo = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    r = requests.get(url)

    json = r.json()
    for commit in json[:10]:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))


if __name__ == "__main__":
    main()
