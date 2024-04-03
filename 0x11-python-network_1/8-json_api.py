#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


def main():
    """
    Main function for the script
    """

    import requests
    from sys import argv

    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}

    r = requests.post(url, data=payload)
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
