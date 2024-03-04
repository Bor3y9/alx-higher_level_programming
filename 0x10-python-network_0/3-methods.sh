#!/bin/bash
# Display croissant
curl -sI "$1" | grep 'Allow' | cut -d: -f2 | cut -d ' ' -f2-
