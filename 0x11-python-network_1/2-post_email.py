#!/usr/bin/python3
"""
2-post_email module
Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    """
    Send a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    url = sys.argv[1]
    value = {"email" : sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
