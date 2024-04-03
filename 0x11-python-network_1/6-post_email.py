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
    
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    data = {"email": email}

    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    main()
