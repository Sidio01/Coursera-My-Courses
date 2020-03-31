n = int(input())
i = 0.5
x = i + 1.5
while i <= n:
    i = i * x
    if i > n:
        break
    print(round(i), end=' ')
# Доработать
