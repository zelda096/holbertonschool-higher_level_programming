#!/usr/bin/python3
def add_attribute(ob, nm, val):

    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, nm, val)
