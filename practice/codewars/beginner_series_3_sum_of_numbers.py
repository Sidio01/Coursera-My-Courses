"""
Given two integers a and b, which can be positive or negative, find the sum 
of all the integers between including them too and return it. If the two 
numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""

from icecream import ic


def get_sum(a, b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a
    x = list(range(a, (b + 1)))
    sum = 0
    for num in x:
        sum += num
    return sum


get_sum(1, 3)
get_sum(-1, 2)
get_sum(1, 1)
