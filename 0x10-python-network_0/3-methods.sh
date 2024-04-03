#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow" -i | cut -d ' ' -f2-
