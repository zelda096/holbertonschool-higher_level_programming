#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    long = len(new_list)
    for i in range(long):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
