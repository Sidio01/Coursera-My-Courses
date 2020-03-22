import sys

digit_string = sys.argv
a = len(sys.argv[1])
i = 0
result = 0
while i < a:
    result += int(sys.argv[1][i])
    i += 1
print(result)
