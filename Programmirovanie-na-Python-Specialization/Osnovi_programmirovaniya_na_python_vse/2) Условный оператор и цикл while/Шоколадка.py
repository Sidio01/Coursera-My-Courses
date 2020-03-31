n = int(input())
m = int(input())
k = int(input())
if k < (n * m):
    if k >= n and k % n == 0:
        print('YES')
    elif k >= m and k % m == 0:
        print('YES')
    elif k <= n and n % k == 0:
        print('NO')
    elif k <= m and m % k == 0:
        print('NO')
    else:
        print('NO')
else:
    print('NO')
