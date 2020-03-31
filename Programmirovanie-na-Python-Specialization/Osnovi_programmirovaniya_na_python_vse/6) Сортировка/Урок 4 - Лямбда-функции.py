points = [(1, 1),
          (5, 1),
          (10, 10)
          ]
points.sort(key=lambda p: p[0]**2 + p[1]**2)
print(*points)

x = [1, 5, 2, 3]
y = list(map(lambda x: x**2, x))
print(*y)
