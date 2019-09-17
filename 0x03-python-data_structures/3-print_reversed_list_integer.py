#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rever = my_list[:]
    rever.reverse()
    for i in range(len(rever)):
        print("{:d}".format(rever[i]))
