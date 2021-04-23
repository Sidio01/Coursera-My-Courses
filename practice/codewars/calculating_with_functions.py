"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""

from icecream import ic

def zero(x=None):
    if x is None:
        return '0'
    else:
        return eval('0' + x)
def one(x=None): 
    if x is None:
        return '1'
    else:
        return eval('1' + x)
def two(x=None): 
    if x is None:
        return '2'
    else:
        return eval('2' + x)
def three(x=None):
    if x is None:
        return '3'
    else:
        return eval('3' + x)
def four(x=None):
    if x is None:
        return '4'
    else:
        return eval('4' + x)
def five(x=None):
    if x is None:
        return '5'
    else:
        return eval('5' + x)
def six(x=None):
    if x is None:
        return '6'
    else:
        return eval('6' + x)
def seven(x=None): 
    if x is None:
        return '7'
    else:
        return eval('7' + x)
def eight(x=None):
    if x is None:
        return '8'
    else:
        return eval('8' + x)
def nine(x=None):
    if x is None:
        return '9'
    else:
        return eval('9' + x)

def plus(x=None):
    return '+' + x
def minus(x=None):
    return '-' + x
def times(x=None):
    return '*' + x
def divided_by(x=None):
    return '//' + x


ic(seven(times(five()))) # 35
ic(four(plus(nine()))) # 13
ic(eight(minus(three()))) # 5
ic(six(divided_by(two()))) # 3
