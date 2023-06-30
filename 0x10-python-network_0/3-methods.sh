#!/bin/bash

# Check if URL is provided
if [ $# -eq 0 ]; then
  echo "Error: URL is required."
  exit 1
fi

# Get URL from command line argument
url=$1

# Make a request to the server and retrieve the allowed HTTP methods
methods=$(curl -s -I -X OPTIONS "$url" | awk '/Allow:/ {print $2}')

# Check if the request was successful
if [ $? -ne 0 ]; then
  echo "Error: Failed to retrieve the supported HTTP methods."
  exit 1
fi

# Display the supported HTTP methods
echo "Supported HTTP methods for $url:"
echo "$methods"

