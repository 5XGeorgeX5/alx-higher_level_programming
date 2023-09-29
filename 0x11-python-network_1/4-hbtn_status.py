#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
