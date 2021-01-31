n = int(input())
nMax1 = 0
nMax2 = 0
if nMax1 > nMax2:
    nMax2, nMax1 = nMax1, nMax2
while n != 0:
    if n > nMax1:
        nMax1, nMax2 = n, nMax1
    elif n > nMax2:
        nMax2 = n
    n = int(input())
print(nMax2)
