#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    y = 0
    while z < x:
        try:
            print("{:d}".format(my_list[z]), end="")
            y += 1
        except ValueError:
            pass
        except TypeError:
            pass
        z += 1
    print()
    return y
