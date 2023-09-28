#!/bin/bash
# sends a JSON POST request to a passed URL, and displays the body of the response.
curl -sLX POST -d "@$2" -H "Content-Type: application/json" "$1"
