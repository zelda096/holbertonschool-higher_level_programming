#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    my_list.reverse()
    for e in my_list:
        print('{:d}'.format(e))
