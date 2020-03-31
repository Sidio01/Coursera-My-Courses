a = int(input())
if a % 3 == 0 or a % 5 == 0:
    print('YES')
elif a % 5 == 3 and a % 3 == 2:
    print('YES')
elif a % 5 == 3 and a % 27 != 0:
    print('YES')
elif a % 50 != 0 and (a % 50) % 3 == 0:
    print('YES')
elif a % 100 != 0 and (a % 100) % 3 == 0:
    print('YES')
elif a % 10 == 3 or a % 10 == 5 or a % 10 == 6 or a % 10 >= 7:
    print('YES')
else:
    print('NO')
