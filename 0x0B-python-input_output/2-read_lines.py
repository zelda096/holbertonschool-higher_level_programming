#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):

    c = 0
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines > 0:
            for line in f:
                if c < nb_lines:
                    print(line, end='')
                    c += 1
                else:
                    break
        else:
            for line in f:
                print(line, end='')
