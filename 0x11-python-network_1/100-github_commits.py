#!/usr/bin/python3
"""
100-github_commits module
Usage: ./100-github_commits.py <repository name> <repository name>
"""
import sys
import requests


if __name__ == "__main__":
    """
    List 10 commits from most recent to older of the repositiory
    'rails' by the user 'rails'
    """

    url = "https://developer.github.com/v3/repos/commits/".format(
            sys.argv[1], sys.argv[2])
    r = request.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                  commits[i].get("sha"),
                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
