#!/bin/bash
# Send a header value with the request
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
