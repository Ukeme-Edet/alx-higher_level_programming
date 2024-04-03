#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""


def main():
    """
    This function takes in a URL, sends a request to the URL and displays the
    body of the response (decoded in utf-8).
    """
    import requests
    from sys import argv

    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
