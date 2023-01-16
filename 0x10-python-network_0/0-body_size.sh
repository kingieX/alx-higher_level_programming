#!/bin/bash
# A bash Script that takes in a URL, sends request to that URl.
curl -s "$1" | wc -c
