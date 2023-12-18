#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        sys.stdout.write("{:d}\n".format(value))
    except (TypeError, ValueError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        sys.stderr.flush()
        return False
    return True
