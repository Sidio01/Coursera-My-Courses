a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == b1 and a2 == b2:
    print('YES')
elif a1 == b1 == a2 or a1 == b1 == b2:
    print('YES')
elif (a1 + b1) == (a2 + b2):
    print('YES')
elif abs(a1 - b1) == abs(a2 - b2):
    print('YES')
elif abs(a1 + b1) == abs(a2 - b2):
    print('YES')
elif abs(a1 - b1) == abs(a2 + b2):
    print('YES')
else:
    print('NO')
