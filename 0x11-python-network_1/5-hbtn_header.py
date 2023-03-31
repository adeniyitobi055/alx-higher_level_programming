#!/usr/bin/python3
"""
5-hbtn_header module
Usage: ./5-hbtn_header.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    """
    Send a request to a URL passed as an argument and displays the value
    of the variable X-Request-Id in the response header
    """
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
