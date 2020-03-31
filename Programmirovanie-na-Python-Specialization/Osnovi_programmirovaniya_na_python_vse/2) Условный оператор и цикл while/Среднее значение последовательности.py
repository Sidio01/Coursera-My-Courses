now = int(input())
sumSeq = now
d = 0
av = 0
while now != 0:
    now = int(input())
    sumSeq += now
    d = d + 1
    av = sumSeq / d
print(av)
