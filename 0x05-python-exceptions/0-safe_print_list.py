#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for rec in my_list:
        try:
            if c < x:
                print("{}".format(rec), end="")
                c += 1
        except():
            continue
    print("")
    return(c)
