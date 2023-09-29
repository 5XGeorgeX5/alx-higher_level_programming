#!/usr/bin/python3
"""takes in a URL, and displays the body of the response"""

if __name__ == "__main__":
    from sys import argv
    import requests

    response = requests.get(argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
