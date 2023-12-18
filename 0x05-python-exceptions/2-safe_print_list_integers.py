#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            ele = my_list[j]
        except IndexError:
            return i
        try:
            print("{:d}".format(ele), end="")
            i += 1
        except (ValueError, TypeError):
            pass
    print()
    return i
