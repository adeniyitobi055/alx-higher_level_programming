#!/usr/bin/python3
"""
6-post_email module
Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    """
    Send a POST request to the URL and email passed as arguments,
    and finally displays the body of the response
    """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, value)
    print(r.text)
