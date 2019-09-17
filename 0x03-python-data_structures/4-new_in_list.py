#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    long = len(copy)

    for i in copy:
        if idx < 0:
            return(copy)
        elif idx > long - 1:
            return(copy)
        elif i == copy[idx]:
            copy[idx] = element
            return(copy)
