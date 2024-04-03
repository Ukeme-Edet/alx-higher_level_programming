#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password) and
uses the Github API to display your id
"""


def main():
    """
    Main function for the script
    """

    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))

    json = r.json()
    print(json.get("id"))


if __name__ == "__main__":
    main()
