#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""


def main():
    """
    This function takes in a URL, sends a request to the URL and displays the
    value of the X-Request-Id variable found in the header of the response.
    """
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))


if __name__ == "__main__":
    main()
