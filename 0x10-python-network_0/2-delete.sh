#!/bin/bash
# Takes in a URL, sends a DELETE request to that URL, and displays the body of the response
curl -sL "$1" -X DELETE
