#!/usr/bin/python3
"""takes in a URL, displays the value of the X-Request-Id"""

if __name__ == "__main__":
    from sys import argv
    import requests

    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
