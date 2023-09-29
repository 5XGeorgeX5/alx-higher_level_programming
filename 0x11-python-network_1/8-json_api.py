#!/usr/bin/python3
"""takes a letter & sends a POST request to http://0.0.0.0:5000/search_user"""

if __name__ == "__main__":
    from sys import argv
    import requests

    data = {'q': argv[1] if len(argv) > 1 else ""}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json = response.json()
        if json:
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
