#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list = my_list
    if idx < 0:
        return (list)

    length = len(list)

    if idx > length - 1:
        return (list)

    my_list[idx] = element

    return (list)
