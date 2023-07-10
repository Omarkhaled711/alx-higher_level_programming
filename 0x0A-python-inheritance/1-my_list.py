#!/usr/bin/python3
"""
This module contains a class "MyList" that inherits from list
"""


class MyList(list):
    """
    This class inherits from list class in python
    """
    def print_sorted(self):
        """
        This function print the list in an ascending order,
        without affecting the original list
        """
        print(sorted(self))
