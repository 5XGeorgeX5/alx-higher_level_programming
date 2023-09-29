#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request,
and displays the body of the response"""

if __name__ == "__main__":
    from sys import argv
    import requests

    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
