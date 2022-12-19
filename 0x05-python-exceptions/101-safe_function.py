#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
