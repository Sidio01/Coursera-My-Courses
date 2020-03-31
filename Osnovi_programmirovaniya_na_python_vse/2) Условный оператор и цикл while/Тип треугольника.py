a = int(input())
b = int(input())
c = int(input())
if a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
    print('rectangular')
elif a + b <= c or a + c <= b or c + b <= a:
    print('impossible')
elif a == b or a == c or b == c:
    print('acute')
elif a == b == c:
    print('acute')
elif a**2 + b**2 > c**2:
    print('acute')
elif a**2 + b**2 < c**2:
    print('obtuse')
elif a**2 + c**2 > b**2:
    print('acute')
elif a**2 + c**2 < b**2:
    print('obtuse')
elif c**2 + b**2 > a**2:
    print('acute')
elif c**2 + b**2 < a**2:
    print('obtuse')
else:
    print('impossible')
