#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_a_dictionary = a_dictionary.copy()
    for i in n_a_dictionary:
        n_a_dictionary[i] = n_a_dictionary[i]*2
    return n_a_dictionary
