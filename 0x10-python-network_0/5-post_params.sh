#!/bin/bash

URL="$1"
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

# Send POST request and store response
RESPONSE=$(curl -s -X POST -d "email=$EMAIL&subject=$SUBJECT" "$URL")

# Display response body
echo "$RESPONSE"
