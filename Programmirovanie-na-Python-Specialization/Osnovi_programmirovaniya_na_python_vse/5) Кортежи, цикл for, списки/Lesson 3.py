a = [1, 2, 3]
b = a[:]
a[0] = 4
print(a)
print(b)

c = list('abcde')
c[0] = 'f'
s = ''.join(c)
print(s)

wordList = input().split()
print(wordList)

intList = list(map(int, input().split()))
print(intList)

