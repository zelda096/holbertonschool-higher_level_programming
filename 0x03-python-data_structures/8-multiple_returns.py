#!/usr/bin/python3
def multiple_returns(sentence):
    y = len(sentence)
    if y == 0:
        x = None
    else:
        x = sentence[0]
    j = (y, x)
    return(j)
