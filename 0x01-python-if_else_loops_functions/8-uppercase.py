#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            ch = chr(ord(c) - 32)
        else:
            ch = c
        print("{:s}".format(ch), end="")
    print('')
