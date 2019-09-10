#!/usr/bin/python3
for ascii in range(97, 123):
    if ascii != 101 and ascii != 113:
        print("{:c}".format(ascii), end="")
