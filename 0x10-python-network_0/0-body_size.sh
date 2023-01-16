#!/bin/bash
# A bash Script that takes in a URL, sends request to that URl and Displays size of body.

curl -s "$1" | wc -c
