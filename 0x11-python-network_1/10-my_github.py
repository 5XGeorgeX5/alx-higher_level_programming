#!/usr/bin/python3
"""takes yourusername and password on GitHub and display your id"""

if __name__ == "__main__":
    from sys import argv
    from requests import get

    response = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(response.json().get('id'))
