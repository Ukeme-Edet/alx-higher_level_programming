#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -X GET -H "X-School-User-Id: 98"
