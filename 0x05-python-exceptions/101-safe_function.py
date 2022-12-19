#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Secu
