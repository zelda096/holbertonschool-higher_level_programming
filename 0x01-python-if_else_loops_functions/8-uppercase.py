#!/usr/bin/python3
def uppercase(str):
    for counter in range(len(str)):
        if ord(str[counter]) >= 97 and ord(str[counter]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[counter]) - number), end='')
    print()
