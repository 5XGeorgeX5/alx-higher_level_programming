#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request,
and displays the body of the response"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse

    email = parse.urlencode({'email': argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], data=email) as response:
        print(response.read().decode('utf-8'))
