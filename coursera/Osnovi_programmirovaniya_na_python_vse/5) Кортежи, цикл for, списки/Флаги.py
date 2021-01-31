n = int(input())
print('+___ ' * n)
for b in range(1, n + 1):
    print('|', b, ' / ', sep='', end='')
print()
print('|__\ ' * n)
print('|    ' * n, '')
