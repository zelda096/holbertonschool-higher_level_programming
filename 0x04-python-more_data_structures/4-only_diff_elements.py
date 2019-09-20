#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    n_set1 = set(set_1)
    n_set2 = set(set_2)

    return n_set1 ^ n_set2
