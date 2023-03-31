#!/usr/bin/python3
"""
8-json_api module
Usage: ./8-json_apy.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    """
    Sends a POST request to http://0.0.0.0:5000/search_user
    with the letter passed as an argument
    """
    letter = "" if len(sys.argv) == 1 else (sys.argv[1])
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
