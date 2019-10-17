#!/usr/bin/python3
def number_of_lines(filename=""):

    with open(filename, 'r', encoding="utf-8") as f:
        c = 0
        for line in f:
            c += 1
    return c
