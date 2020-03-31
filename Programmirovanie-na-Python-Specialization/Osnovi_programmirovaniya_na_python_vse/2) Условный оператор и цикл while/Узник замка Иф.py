a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
s1 = a * b
s2 = b * c
s3 = a * c
s4 = d * e
x = a <= b <= c
y = c <= b <= a
z = a <= c <= b
if (x or b <= a <= c) and (a <= d <= e or b <= e <= d) and s1 <= s4:
    print('YES')
elif (y or b <= c <= a) and (c <= d <= e or b <= e <= d) and s2 <= s4:
    print('YES')
elif (z or c <= a <= b) and (c <= d <= e or a <= e <= d) and s3 <= s4:
    print('YES')
else:
    print('NO')
