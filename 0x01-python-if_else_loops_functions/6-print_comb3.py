#!/usr/bin/python3
for comb in range(0, 90):
        if comb % 10 > comb / 10:
                if comb != 89:
                        print("{:02d}, ".format(comb), end='')
                else:
                        print("{:02d}".format(comb))
