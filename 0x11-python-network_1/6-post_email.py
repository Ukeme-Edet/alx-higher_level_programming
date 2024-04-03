#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""


def main():
    """
    This function takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
    """
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
