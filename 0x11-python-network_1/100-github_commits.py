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
    for i in range(10):
        try:
            commit = json[i].get("commit")
            author = commit.get("author")
            print("{}: {}".format(json[i].get("sha"), author.get("name")))
        except IndexError:
            break


if __name__ == "__main__":
    main()
