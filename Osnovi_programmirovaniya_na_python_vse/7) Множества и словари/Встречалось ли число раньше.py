myList = list(map(int, input().split()))
a = set()
c = 0
for i in myList:
    b = myList[c]
    if b in a:
        print('YES')
        c += 1
    else:
        print('NO')
        a.add(b)
        c += 1
