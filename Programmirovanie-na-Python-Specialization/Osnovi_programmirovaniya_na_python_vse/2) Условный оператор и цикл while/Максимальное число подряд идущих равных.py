n = int(input())
cl = 0
ml = 0
d = -1
while n != 0:
    if d == n:
        cl += 1
    else:
        d = n
        ml = max(ml, cl)
        cl = 1
    n = int(input())
ml = max(ml, cl)
print(ml)
