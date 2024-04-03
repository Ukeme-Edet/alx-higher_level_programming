#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the status code of the response
curl -sI -w "%{response_code}" "$1" -o /dev/null
