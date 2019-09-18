#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)

    if len(a) < 2:
        for i in range(len(a), 2):
            a.append(0)

    if len(b) < 2:
        for i in range(len(b), 2):
            b.append(0)

    r = [a[0] + b[0], a[1] + b[1]]
    return (tuple(r))
