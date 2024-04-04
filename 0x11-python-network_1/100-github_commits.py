#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
"""


def main():
    """
    Main function for the script
    """

    import requests
    from sys import argv

    username, repo = argv[1], argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)

    r = requests.get(url)
    commits = r.json()

    print(username, repo, commits)
    # try:
    #     for i in range(10):
    #         print(
    #             "{}: {}".format(
    #                 commits[i].get("sha"),
    #                 commits[i].get("commit").get("author").get("name")
    #             )
    #         )
    # except IndexError:
    #     pass


if __name__ == "__main__":
    main()
