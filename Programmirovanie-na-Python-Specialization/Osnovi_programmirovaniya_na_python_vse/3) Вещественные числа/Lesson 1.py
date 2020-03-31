x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('Equal')
else:
    print('Not equal')
print('{0:.25f}'.format(0.1))
print(0.1.as_integer_ratio())
