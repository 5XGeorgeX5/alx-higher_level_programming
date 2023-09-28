#!/bin/bash
# sends a request to the passed URL, and displays only the status code of the response.
curl -sLo /dev/null -w "%{http_code}" "$1"
