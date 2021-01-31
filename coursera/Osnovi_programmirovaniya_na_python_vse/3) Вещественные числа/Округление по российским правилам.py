import math
n = float(input())
x = round(n - int(n), 6)
if x >= 0.5:
    print(math.ceil(n))
else:
    print(int(n))
