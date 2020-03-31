a = [3, 1, 2]
a.sort()
b = sorted(a, reverse=True)
print(*b)
print((1, 2) < (3, 4))

p = [(172, 'Vasya'),
     (180, 'Petya'),
     (172, 'Fedya')]
p.sort(reverse=True)
print(p)
