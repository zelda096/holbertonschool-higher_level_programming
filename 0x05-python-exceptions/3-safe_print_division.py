#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return None
    finally:
        try:
            print("Inside result: {:0.1f}".format(x))
        except UnboundLocalError:
            print("Inside result: {}".format(None))
