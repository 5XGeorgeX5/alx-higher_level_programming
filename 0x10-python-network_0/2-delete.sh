#!/bin/bash
# sends a DELETE request to the passed URL and displays the body of the response
curl -sLX DELETE "$1"
