#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    checks instance
    """
    return isinstance(obj, a_class) and obj.__class__ != a_class
