#!/usr/bin/python3

"""
The module function: text_indentation().

"""


def text_indentation(text):
    """
    Arguments:
    text: string
    """
    err = "text must be a string"
    if not isinstance(text, str):
        raise TypeError(err)

    if text is None:
        raise TypeError(err)

    if len(text) < 0:
        raise TypeError(err)

    text = text.replace('.', '.\\')
    text = text.replace('?', '?\\')
    text = text.replace(':', ':\\')

    print('\n\n'.join([t.strip() for t in text.split('\\')]), end="")
