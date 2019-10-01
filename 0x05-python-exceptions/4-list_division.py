#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = 0
    y = []
    while x < list_length:
        z = 0
        try:
            z = (my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            print("division by 0")
            pass
        except TypeError:
            print("wrong type")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            y.append(z)
        x += 1
    return y
