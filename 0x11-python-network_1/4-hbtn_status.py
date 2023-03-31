#!/usr/bin/python3
"""
4-hbtn_status module
Usage: ./4-hbtn_status.py | cat -e
"""
import requests


if __name__ == "__main__":
    """ Fetches http://alx-intranet.hbtn.io/status """
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
