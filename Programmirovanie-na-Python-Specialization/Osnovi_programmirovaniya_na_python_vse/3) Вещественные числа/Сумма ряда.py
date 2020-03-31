n = float(input())
i = 1
s = 1
while i < n:
    i += 1
    s = s + (1 / i ** 2)
print('{0:.6f}'.format(s))
