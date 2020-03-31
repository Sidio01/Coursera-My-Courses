n = int(input())
i = 1
x = i
while i <= n:
    i = i + 1
    if n % i == 0:
        break
print(i)
