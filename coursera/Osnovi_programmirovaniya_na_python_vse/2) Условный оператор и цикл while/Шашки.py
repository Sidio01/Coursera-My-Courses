v1 = int(input())
h1 = int(input())
v2 = int(input())
h2 = int(input())
if h2 > h1:
    if (v1 + h1) == (v2 + h2):
        print('YES')
    elif abs(v1 - h1) == abs(v2 - h2):
        print('YES')
    elif abs(v1 + h1) == abs(v2 - h2):
        print('YES')
    elif abs(v1 - h1) == abs(v2 + h2):
        print('YES')
    elif v1 == h1 and abs(v2 - h2) == 2:
        print('YES')
    elif v1 == v2 and abs(h2 - h1) != 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
