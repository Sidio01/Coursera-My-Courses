import sys

digit_string = sys.argv
a = int(sys.argv[1])
i = 1
while i <= a:
    print(" " * (a - i) + '#' * i)
    i += 1
