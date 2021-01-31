"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square 
after the one passed as a parameter. Recall that an integral perfect square 
is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. 
You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
"""
import math
from icecream import ic


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if math.sqrt(sq).is_integer():
        return (math.sqrt(sq) + 1)**2
    else:
        return -1


find_next_square(121)
find_next_square(625)
find_next_square(114)
