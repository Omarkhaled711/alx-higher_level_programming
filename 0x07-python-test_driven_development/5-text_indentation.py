#!/usr/bin/python3
"""
text_identation module, it contains one functions, which
is text_identation(), it prints 2  new lines when it encounters
these special chars (. ? : )
"""


def text_indentation(text):
    """
    a function that prints 2 new lines when it encounters
    these special chars (. ? : ). It accepts string args,
    if the argument is of any other type, a TypeError is raised
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for letter in text:
        print(letter, end='')
        if letter == '.' or letter == '?' or letter == ':':
            print('\n')
