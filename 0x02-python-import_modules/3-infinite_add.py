#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = len(sys.argv) - 1
    product = 0

    for arguments in range(counter):
        product  = product + int(sys.argv[arguments + 1])
    print(product)
