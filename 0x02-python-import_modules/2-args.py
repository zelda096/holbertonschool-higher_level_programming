#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = len(sys.argv) - 1

    if counter == 0:
        print("{} arguments.".format(counter))

    elif counter == 1:
        print("{} argument:".format(counter))

    else:
        print("{} arguments:".format(counter))

    if counter >=1:
        counter = 0

        for arguments in sys.argv:
            if counter != 0:
                print("{}: {}".format(counter, arguments))
            counter += 1
