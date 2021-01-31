x1 = int(input())
y = int(input())
x2 = x1
d = 1
if y <= x2:
    print(1)
while x2 < y:
    x2 = x2 * 1.1
    d = d + 1
    if x2 >= y:
        print(d)
