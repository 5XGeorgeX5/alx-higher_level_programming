#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except:
        print(f"Exception: {sys.exc_info()[1]}", file=sys.stderr)
        return None
