#!/usr/bin/python3
"""takes in a URL, displays the value of the X-Request-Id."""

if __name__ == "__main__":
    from sys import argv
    from urllib import request

    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
