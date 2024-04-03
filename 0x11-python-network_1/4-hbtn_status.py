#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""


def main():
    """
    This function fetches https://intranet.hbtn.io/status
    """
    import requests

    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
