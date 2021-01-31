a = 1
b = 2
a, b = b, a
print(a, b)
myRange = range(10)
print(tuple(myRange))
for color in ('red', 'green', 'yellow'):
    print(color, 'apple', end=' ')
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()
