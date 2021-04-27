"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""

from icecream import ic

def bool_to_word(boolean):
    return 'Yes' if boolean is True else 'No'

ic(bool_to_word(True))
ic(bool_to_word(False))