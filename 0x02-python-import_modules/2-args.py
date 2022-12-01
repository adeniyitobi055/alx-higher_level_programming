#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArg = len(sys.argv)
    if numArg == 1:
        print("{} arguments.".format(numArg - 1))
    elif numArg == 2:
        print("{} argument:".format(numArg - 1))
    else:
        print("{} arguments:".format(numArg - 1))

    for i in range(1, numArg):
        print("{}: {}".format(i, sys.argv[i]))
