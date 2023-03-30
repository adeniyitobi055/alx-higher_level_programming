#!/bin/bash
# Displays only the status code of the response of the URL passed as an argument
curl -s -o /dev/null -w "%{http_code}" "$1"
